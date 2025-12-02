
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1& 
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3& 
    (38, 1.5, 0.375),   # Snare on 4
    (42, 1.5, 0.1875)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (walking line, chromatic approaches)
bass_notes = [
    (36, 1.5, 0.375),   # D (root)
    (38, 1.875, 0.375), # Eb (chromatic approach)
    (37, 2.25, 0.375),  # C (3rd)
    (39, 2.625, 0.375), # D (5th)
    (40, 3.0, 0.375),   # Eb (7th)
    (38, 3.375, 0.375), # D (chromatic approach)
    (37, 3.75, 0.375),  # C (3rd)
    (36, 4.125, 0.375), # D (5th)
    (35, 4.5, 0.375),   # C (chromatic approach)
    (34, 4.875, 0.375), # B (7th)
    (35, 5.25, 0.375),  # C (root)
    (36, 5.625, 0.375)  # D (5th)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2
    (48, 1.875, 0.375), # G7 (G, B, D, F)
    (50, 1.875, 0.375),
    (52, 1.875, 0.375),
    (55, 1.875, 0.375),
    # Bar 3
    (48, 3.375, 0.375), # G7 again
    (50, 3.375, 0.375),
    (52, 3.375, 0.375),
    (55, 3.375, 0.375),
    # Bar 4
    (48, 4.875, 0.375), # G7 again
    (50, 4.875, 0.375),
    (52, 4.875, 0.375),
    (55, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Drums: Full bar 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 1& 
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375))
    # Hihat on 2& 
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.75 + 0.1875))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.5, end=start + 1.5 + 0.375))
    # Hihat on 3& 
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.5 + 0.1875))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 2.25, end=start + 2.25 + 0.375))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 2.25, end=start + 2.25 + 0.1875))

# Sax: Dante (melody)
sax_notes = [
    (61, 1.5, 0.375),   # F (start with root)
    (63, 1.875, 0.375), # G (chromatic up)
    (61, 2.25, 0.375),  # F (back to root)
    (62, 2.625, 0.375), # F# (suspended)
    (60, 3.0, 0.375),   # E (major 7th)
    (62, 3.375, 0.375), # F# (chromatic)
    (60, 3.75, 0.375),  # E (back to 7th)
    (61, 4.125, 0.375), # F (root)
    (63, 4.5, 0.375),   # G (chromatic)
    (61, 4.875, 0.375), # F (root)
    (62, 5.25, 0.375),  # F# (suspended)
    (60, 5.625, 0.375)  # E (7th)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
