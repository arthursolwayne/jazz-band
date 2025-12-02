
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
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

# Bass line: walking line in D, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), # D4 on 1
    (64, 1.875, 0.375), # F#4 on 2
    (65, 2.25, 0.375), # G4 on 3
    (62, 2.625, 0.375), # D4 on 4
    (65, 3.0, 0.375), # G4 on 1
    (67, 3.375, 0.375), # A4 on 2
    (69, 3.75, 0.375), # B4 on 3
    (67, 4.125, 0.375), # A4 on 4
    (69, 4.5, 0.375), # B4 on 1
    (67, 4.875, 0.375), # A4 on 2
    (65, 5.25, 0.375), # G4 on 3
    (62, 5.625, 0.375) # D4 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (62, 1.875, 0.1875), # D7 (D, F#, A, C#)
    (64, 1.875, 0.1875),
    (69, 1.875, 0.1875),
    (67, 1.875, 0.1875),
    # Bar 3
    (62, 3.375, 0.1875), # D7
    (64, 3.375, 0.1875),
    (69, 3.375, 0.1875),
    (67, 3.375, 0.1875),
    # Bar 4
    (62, 4.875, 0.1875), # D7
    (64, 4.875, 0.1875),
    (69, 4.875, 0.1875),
    (67, 4.875, 0.1875),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.375 + 0.375))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.375 + 0.1875))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.75 + 0.375))
    # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.75 + 0.1875))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.125 + 0.375))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.125 + 0.1875))

# Sax: Motif in D, short and singing
sax_notes = [
    (65, 1.5, 0.375), # G4 (1st beat)
    (67, 1.875, 0.375), # A4 (2nd beat)
    (72, 2.25, 0.375), # D5 (3rd beat)
    (67, 2.625, 0.375), # A4 (4th beat)
    (65, 3.0, 0.375), # G4 (1st beat)
    (67, 3.375, 0.375), # A4 (2nd beat)
    (69, 3.75, 0.375), # B4 (3rd beat)
    (67, 4.125, 0.375), # A4 (4th beat)
    (65, 4.5, 0.375), # G4 (1st beat)
    (67, 4.875, 0.375), # A4 (2nd beat)
    (69, 5.25, 0.375), # B4 (3rd beat)
    (67, 5.625, 0.375) # A4 (4th beat)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
