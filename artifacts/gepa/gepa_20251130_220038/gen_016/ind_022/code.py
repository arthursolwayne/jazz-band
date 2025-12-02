
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
    (42, 0.5), (42, 0.625), (42, 0.75), (42, 0.875), (36, 1.125), (38, 1.5),
    (42, 1.125), (42, 1.25), (42, 1.375), (42, 1.5)
]

for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    # Bar 2
    (48, 1.5), (50, 1.875), (48, 2.25), (51, 2.625),
    # Bar 3
    (53, 3.0), (51, 3.375), (50, 3.75), (48, 4.125),
    # Bar 4
    (49, 4.5), (51, 4.875), (53, 5.25), (55, 5.625)
]

for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.75), (64, 1.75), (67, 1.75), (71, 1.75),
    # Bar 3
    (62, 3.25), (66, 3.25), (69, 3.25), (72, 3.25),
    # Bar 4
    (64, 4.75), (68, 4.75), (71, 4.75), (74, 4.75)
]

for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Sax: short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2
    (62, 1.5), (65, 1.875), (67, 2.25),
    # Bar 3
    (65, 3.0), (62, 3.375),
    # Bar 4
    (67, 4.5), (65, 4.875), (62, 5.25)
]

for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
