
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.875), (39, 2.25), (43, 2.625),
    (43, 3.0), (45, 3.375), (44, 3.75), (48, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, one chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (65, 1.5), (68, 1.5), (60, 1.5), (64, 1.5),
    # Bar 3: Em7 (E, G, Bb, D)
    (64, 3.0), (67, 3.0), (69, 3.0), (62, 3.0),
    # Bar 4: D7 (D, F#, A, C)
    (62, 4.5), (67, 4.5), (69, 4.5), (60, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Drums: same pattern as bar 1
for note, time in drum_notes:
    if time >= 1.5:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time + 1.5, end=time + 1.5 + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: F, G, A, Bb (F, G, A, Bb) on 1, 2, 3, & (end of 4)
sax_notes = [
    (65, 1.5), (66, 1.875), (67, 2.25), (67, 2.625),
    (65, 3.0), (66, 3.375), (67, 3.75), (67, 4.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Bar 3: No sax, just bass and piano
# Bar 4: Back to sax, complete the motif
sax_notes = [
    (65, 4.5), (66, 4.875), (67, 5.25), (67, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
