
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5s - 3.0s)

# Marcus (bass): walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5s)
    (50, 1.5), (53, 1.75), (52, 2.0), (50, 2.25),
    # Bar 3 (2.25s)
    (50, 2.25), (53, 2.5), (52, 2.75), (50, 3.0),
    # Bar 4 (3.0s)
    (50, 3.0), (53, 3.25), (52, 3.5), (50, 3.75)
]

for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane (piano): open voicings, different chord each bar, comp on 2 and 4
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    # Bar 2 (1.5s)
    (53, 1.5), (55, 1.5), (58, 1.5), (60, 1.5),  # Dm7
    # Bar 3 (2.25s)
    (53, 2.25), (55, 2.25), (57, 2.25), (61, 2.25),  # C7
    # Bar 4 (3.0s)
    (53, 3.0), (55, 3.0), (58, 3.0), (61, 3.0)   # Gm7
]

for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Little Ray (drums): kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5s - 3.0s)
for i in range(2):
    bar_start = 1.5 + i * 1.5
    drum_notes = [
        (36, bar_start), (38, bar_start + 0.375), (42, bar_start + 0.375),
        (36, bar_start + 0.75), (38, bar_start + 1.125), (42, bar_start + 1.125),
        (36, bar_start + 1.5), (38, bar_start + 1.875), (42, bar_start + 1.875)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante (sax): start with a haunting motif, leave it hanging, then finish
# Motif: D (E4), Bb (D4), F (F4), rest
# Then repeat the motif an octave up, but end on D (E5) with a rest

sax_notes = [
    # Bar 2 (1.5s)
    (62, 1.5), (60, 1.75), (65, 2.0),
    # Bar 3 (2.25s)
    (62, 2.25), (60, 2.5), (65, 2.75),
    # Bar 4 (3.0s)
    (67, 3.0), (65, 3.25), (70, 3.5)
]

for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Add rest at the end
sax.notes.append(pretty_midi.Note(velocity=0, pitch=62, start=3.5, end=3.75))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
