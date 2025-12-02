
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches
bass_notes = [
    (65, 1.5), (67, 1.875), (64, 2.25), (62, 2.625),
    (65, 2.875), (67, 3.25), (64, 3.625), (62, 4.0),
    (65, 4.25), (67, 4.625), (64, 5.0), (62, 5.375)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (67, 2.0), (71, 2.0), (64, 2.0), (69, 2.0),  # D7
    (72, 2.5), (76, 2.5), (69, 2.5), (74, 2.5),  # G7
    # Bar 3
    (67, 3.0), (71, 3.0), (64, 3.0), (69, 3.0),  # D7
    (72, 3.5), (76, 3.5), (69, 3.5), (74, 3.5),  # G7
    # Bar 4
    (67, 4.0), (71, 4.0), (64, 4.0), (69, 4.0),  # D7
    (72, 4.5), (76, 4.5), (69, 4.5), (74, 4.5)   # G7
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Saxophone (Dante): One short motif, make it sing
sax_notes = [
    (62, 1.5), (64, 1.75), (62, 2.0),  # Bar 2
    (64, 2.25), (65, 2.5), (62, 2.75),  # Bar 3
    (64, 3.0), (62, 3.25), (64, 3.5), (65, 3.75),  # Bar 4
    (67, 4.0), (64, 4.25), (65, 4.5), (64, 4.75),  # Bar 4
    (62, 5.0)  # End on D
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
