
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.1875), (42, 0.375), (42, 0.5625),
    (42, 0.75), (42, 0.9375), (42, 1.125), (42, 1.3125), (36, 1.5), (38, 1.875), 
    (42, 1.5), (42, 1.6875), (42, 1.875), (42, 2.0625), (42, 2.25), (42, 2.4375),
    (42, 2.625), (42, 2.8125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Sax: One short motif, start it, leave it hanging, come back and finish it
# Fm scale: F, Gb, Ab, Bb, B, Db, Eb
sax_notes = [
    # Bar 2
    (84, 1.5), (82, 1.75), (81, 2.0), (80, 2.25),
    # Bar 3, leave it hanging
    (84, 3.0), (82, 3.25), (81, 3.5),
    # Bar 4, finish it
    (80, 4.0), (84, 4.25), (82, 4.5), (81, 4.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line, chromatic approaches, no repeated notes
# Fm7: F, Ab, Bb, Db
bass_notes = [
    # Bar 2
    (53, 1.5), (51, 1.75), (50, 2.0), (49, 2.25),
    # Bar 3
    (53, 3.0), (52, 3.25), (51, 3.5), (50, 3.75),
    # Bar 4
    (53, 4.0), (51, 4.25), (50, 4.5), (49, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
# Fm7: F, Ab, Bb, Db
piano_notes = [
    # Bar 2, comp on beat 2
    (53, 1.75), (51, 1.75), (50, 1.75), (49, 1.75),
    # Bar 3, comp on beat 2
    (53, 3.25), (51, 3.25), (50, 3.25), (49, 3.25),
    # Bar 4, comp on beat 2
    (53, 4.25), (51, 4.25), (50, 4.25), (49, 4.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
