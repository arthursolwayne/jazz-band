
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (44, 1.5, 0.375), (45, 1.875, 0.375), (43, 2.25, 0.375), (42, 2.625, 0.375),
    (44, 3.0, 0.375), (45, 3.375, 0.375), (43, 3.75, 0.375), (42, 4.125, 0.375),
    (44, 4.5, 0.375), (45, 4.875, 0.375), (43, 5.25, 0.375), (42, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (57, 1.875, 0.1875), (60, 1.875, 0.1875), (64, 1.875, 0.1875), (62, 1.875, 0.1875),
    (57, 2.625, 0.1875), (60, 2.625, 0.1875), (64, 2.625, 0.1875), (62, 2.625, 0.1875),
    # Bar 3
    (57, 3.375, 0.1875), (60, 3.375, 0.1875), (64, 3.375, 0.1875), (62, 3.375, 0.1875),
    (57, 4.125, 0.1875), (60, 4.125, 0.1875), (64, 4.125, 0.1875), (62, 4.125, 0.1875),
    # Bar 4
    (57, 4.875, 0.1875), (60, 4.875, 0.1875), (64, 4.875, 0.1875), (62, 4.875, 0.1875),
    (57, 5.625, 0.1875), (60, 5.625, 0.1875), (64, 5.625, 0.1875), (62, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Sax: Motif in Fm, short and singable, start at bar 2
sax_notes = [
    (59, 1.875, 0.375),  # Fm7: F, Ab, Bb, D
    (61, 2.25, 0.375),   # Bb
    (58, 2.625, 0.375),  # Eb
    (59, 3.0, 0.375),    # F
    (62, 3.375, 0.375),  # C
    (59, 3.75, 0.375),   # F
    (58, 4.125, 0.375),  # Eb
    (59, 4.5, 0.375),    # F
    (61, 4.875, 0.375),  # Bb
    (59, 5.25, 0.375),   # F
    (62, 5.625, 0.375),  # C
]

for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
