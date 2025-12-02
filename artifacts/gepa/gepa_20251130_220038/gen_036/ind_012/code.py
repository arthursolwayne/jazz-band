
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
    (36, 0.0), (38, 0.375), (42, 0.375), (42, 0.75), (42, 1.125), (42, 1.5),
    (36, 1.5), (38, 1.875), (42, 1.875), (42, 2.25), (42, 2.625), (42, 3.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (30, 1.5), (31, 1.75), (29, 2.0), (28, 2.25),
    (30, 2.5), (31, 2.75), (29, 3.0), (28, 3.25),
    (30, 3.5), (31, 3.75), (29, 4.0), (28, 4.25),
    (30, 4.5), (31, 4.75), (29, 5.0), (28, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (42, 2.0), (46, 2.0), (49, 2.0), (51, 2.0),
    # Bar 3
    (42, 3.5), (46, 3.5), (49, 3.5), (51, 3.5),
    # Bar 4
    (42, 5.0), (46, 5.0), (49, 5.0), (51, 5.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Dante: Whisper to cry, one motif, leave it hanging
sax_notes = [
    (42, 1.5), (44, 1.75), (43, 2.0),
    (45, 2.25), (44, 2.5), (42, 2.75),
    (44, 3.0), (46, 3.25), (45, 3.5),
    (43, 3.75), (44, 4.0), (43, 4.25),
    (42, 4.5), (44, 4.75), (46, 5.0), (44, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
