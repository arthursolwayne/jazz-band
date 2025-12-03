
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
    (36, 0.0), (38, 0.375), (42, 0.375),  # 1
    (38, 0.75), (42, 0.75),               # 2
    (36, 1.125), (38, 1.5), (42, 1.5)     # 3 and 4
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet starts (1.5 - 3.0s)

# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (53, 1.5), (55, 1.75), (53, 2.0), (51, 2.25),  # F, Gb, F, Eb
    (53, 2.5), (55, 2.75), (53, 3.0), (51, 3.25)   # F, Gb, F, Eb
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7sus4 -> F7 -> Fm7
piano_notes = [
    # Bar 2: F7sus4 (F, Bb, C, D)
    (53, 1.5), (58, 1.5), (55, 1.5), (57, 1.5),
    # Bar 3: F7 (F, A, C, Eb)
    (53, 2.5), (60, 2.5), (55, 2.5), (51, 2.5),
    # Bar 4: Fm7 (F, Ab, C, Eb)
    (53, 3.5), (57, 3.5), (55, 3.5), (51, 3.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),  # 1
    (38, 2.25), (42, 2.25),               # 2
    (36, 2.625), (38, 3.0), (42, 3.0),    # 3 and 4
    (38, 3.375), (42, 3.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start motif (F, G#, A, Bb)
sax_notes = [
    (53, 1.5), (56, 1.625), (57, 1.75), (58, 1.875),  # motif
    (57, 2.0)  # leave it hanging
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Bar 3: Rest
# Bar 4: Repeat motif, finish it (F, G#, A)
sax_notes = [
    (53, 3.5), (56, 3.625), (57, 3.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
# midi.write disabled
