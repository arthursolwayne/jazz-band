
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
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (36, 1.5), (37, 1.75), (34, 2.0), (35, 2.25),
    (36, 2.5), (37, 2.75), (34, 3.0), (35, 3.25),
    (36, 3.5), (37, 3.75), (34, 4.0), (35, 4.25),
    (36, 4.5), (37, 4.75), (34, 5.0), (35, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (59, 1.75), (60, 1.75), (62, 1.75), (64, 1.75), # F7
    (57, 2.25), (59, 2.25), (60, 2.25), (62, 2.25), # D7
    # Bar 3
    (59, 3.25), (60, 3.25), (62, 3.25), (64, 3.25), # F7
    (57, 3.75), (59, 3.75), (60, 3.75), (62, 3.75), # D7
    # Bar 4
    (59, 4.25), (60, 4.25), (62, 4.25), (64, 4.25), # F7
    (57, 4.75), (59, 4.75), (60, 4.75), (62, 4.75)  # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (60, 1.5), (62, 1.75), (64, 2.0), # start of motif
    (62, 2.5), (60, 2.75), (59, 3.0), # repeat
    (62, 3.5), (64, 3.75), (62, 4.0), # repeat
    (60, 4.5), (62, 4.75), (64, 5.0)  # finish
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
