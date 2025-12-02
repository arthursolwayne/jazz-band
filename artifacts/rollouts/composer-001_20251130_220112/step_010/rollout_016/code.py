
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
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125),
    (42, 1.25), (42, 1.375), (42, 1.5)
]

for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.25), (63, 1.75, 0.25), (60, 2.0, 0.25), (62, 2.25, 0.25),
    # Bar 3 (3.0 - 4.5s)
    (64, 3.0, 0.25), (62, 3.25, 0.25), (60, 3.5, 0.25), (62, 3.75, 0.25),
    # Bar 4 (4.5 - 6.0s)
    (63, 4.5, 0.25), (62, 4.75, 0.25), (60, 5.0, 0.25), (62, 5.25, 0.25)
]

for pitch, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.75, 0.25), (67, 1.75, 0.25), (69, 1.75, 0.25), (71, 1.75, 0.25),
    (62, 2.25, 0.25), (67, 2.25, 0.25), (69, 2.25, 0.25), (71, 2.25, 0.25),
    # Bar 3 (3.0 - 4.5s)
    (62, 3.25, 0.25), (67, 3.25, 0.25), (69, 3.25, 0.25), (71, 3.25, 0.25),
    (62, 3.75, 0.25), (67, 3.75, 0.25), (69, 3.75, 0.25), (71, 3.75, 0.25),
    # Bar 4 (4.5 - 6.0s)
    (62, 4.75, 0.25), (67, 4.75, 0.25), (69, 4.75, 0.25), (71, 4.75, 0.25),
    (62, 5.25, 0.25), (67, 5.25, 0.25), (69, 5.25, 0.25), (71, 5.25, 0.25)
]

for pitch, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Sax (Dante): Melody. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.25), (65, 1.75, 0.25), (67, 2.0, 0.25), (65, 2.25, 0.25),
    # Bar 3 (3.0 - 4.5s)
    (62, 3.5, 0.25), (65, 3.75, 0.25), (67, 4.0, 0.25), (65, 4.25, 0.25),
    # Bar 4 (4.5 - 6.0s)
    (62, 5.0, 0.25), (65, 5.25, 0.25), (67, 5.5, 0.25), (65, 5.75, 0.25)
]

for pitch, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Drums: Bar 2 - 4 (1.5 - 6.0s)
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.25), (42, 2.375), (42, 2.5), (42, 2.625),
    (42, 2.75), (42, 2.875), (42, 3.0),
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 3.75), (42, 3.875), (42, 4.0), (42, 4.125),
    (42, 4.25), (42, 4.375), (42, 4.5),
    # Bar 4
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.25), (42, 5.375), (42, 5.5), (42, 5.625),
    (42, 5.75), (42, 5.875), (42, 6.0)
]

for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
