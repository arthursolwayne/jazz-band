
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
    (36, 1.125), (38, 1.5), (42, 1.5),
    (36, 2.0), (38, 2.375), (42, 2.375),
    (36, 3.125), (38, 3.5), (42, 3.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5), (63, 1.875), (60, 2.25), (61, 2.625),
    (62, 3.0), (63, 3.375), (60, 3.75), (61, 4.125),
    (62, 4.5), (63, 4.875), (60, 5.25), (61, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.875), (67, 1.875), (71, 1.875), (72, 1.875),
    (64, 3.0), (67, 3.0), (71, 3.0), (72, 3.0),
    # Bar 3
    (64, 3.875), (67, 3.875), (71, 3.875), (72, 3.875),
    # Bar 4
    (64, 5.0), (67, 5.0), (71, 5.0), (72, 5.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Dante: Motif - 1 short phrase, make it sing, leave it hanging
sax_notes = [
    (62, 1.5), (64, 1.75), (62, 2.0), (60, 2.25),
    (62, 2.5), (64, 2.75), (62, 3.0), (60, 3.25),
    (62, 3.5), (64, 3.75), (62, 4.0), (60, 4.25),
    (64, 4.5), (62, 4.75), (60, 5.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
