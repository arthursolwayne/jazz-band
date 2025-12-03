
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2 on 1
    (43, 1.875, 0.375), # G2 on 2
    (42, 2.25, 0.375),  # F2 on 3 (chromatic approach)
    (38, 2.625, 0.375), # D2 on 4
    (43, 3.0, 0.375),   # G2 on 1
    (45, 3.375, 0.375), # A2 on 2
    (43, 3.75, 0.375),  # G2 on 3
    (38, 4.125, 0.375), # D2 on 4
    (43, 4.5, 0.375),   # G2 on 1
    (40, 4.875, 0.375), # Bb2 on 2
    (38, 5.25, 0.375),  # D2 on 3
    (38, 5.625, 0.375)  # D2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, resolve on the last
piano_notes = [
    # Bar 2 (Dm7)
    (62, 1.5, 0.1875), # F4
    (67, 1.5, 0.1875), # A4
    (64, 1.5, 0.1875), # G4
    (60, 1.5, 0.1875), # D4
    # Bar 3 (G7)
    (67, 2.25, 0.1875), # A4
    (71, 2.25, 0.1875), # D5
    (69, 2.25, 0.1875), # F#4
    (67, 2.25, 0.1875), # A4
    # Bar 4 (Cm7)
    (60, 3.0, 0.1875), # D4
    (65, 3.0, 0.1875), # G4
    (63, 3.0, 0.1875), # F4
    (58, 3.0, 0.1875), # C4
    # Bar 2 (comp on 2 and 4)
    (62, 1.875, 0.1875), # F4
    (67, 1.875, 0.1875), # A4
    (64, 1.875, 0.1875), # G4
    (60, 1.875, 0.1875), # D4
    # Bar 3 (comp on 2 and 4)
    (67, 3.375, 0.1875), # A4
    (71, 3.375, 0.1875), # D5
    (69, 3.375, 0.1875), # F#4
    (67, 3.375, 0.1875), # A4
    # Bar 4 (comp on 2 and 4)
    (60, 3.75, 0.1875), # D4
    (65, 3.75, 0.1875), # G4
    (63, 3.75, 0.1875), # F4
    (58, 3.75, 0.1875), # C4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),  # F4 on 1
    (65, 1.875, 0.375), # A4 on 2
    (67, 2.25, 0.375),  # Bb4 on 3
    (62, 2.625, 0.375), # F4 on 4
    (65, 3.0, 0.375),   # A4 on 1
    (67, 3.375, 0.375), # Bb4 on 2
    (69, 3.75, 0.375),  # C5 on 3
    (62, 4.125, 0.375), # F4 on 4
    (65, 4.5, 0.375),   # A4 on 1
    (67, 4.875, 0.375), # Bb4 on 2
    (69, 5.25, 0.375),  # C5 on 3
    (62, 5.625, 0.375)  # F4 on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: continue on bars 2-4
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.1875),  # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.1875),  # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
