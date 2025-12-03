
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (38, 1.5), (41, 1.75), (43, 2.0), (40, 2.25),
    # Bar 3 (3.0 - 4.5s)
    (43, 3.0), (41, 3.25), (38, 3.5), (40, 3.75),
    # Bar 4 (4.5 - 6.0s)
    (40, 4.5), (43, 4.75), (41, 5.0), (38, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    (71, 1.5), (74, 1.5), (76, 1.5), (79, 1.5),  # F7
    # Bar 3: Gm7 (G, Bb, D, F)
    (77, 3.0), (79, 3.0), (82, 3.0), (76, 3.0),  # Gm7
    # Bar 4: Cmaj7 (C, E, G, B)
    (72, 4.5), (76, 4.5), (79, 4.5), (82, 4.5)   # Cmaj7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# You: Tenor sax, one short motif, make it sing
# Motif: F (76), A (79), Bb (80), F (76) — leave it hanging
sax_notes = [
    (76, 1.5), (79, 1.75), (80, 2.0), (76, 2.25),
    (76, 3.0), (79, 3.25), (80, 3.5), (76, 3.75),
    (76, 4.5), (79, 4.75), (80, 5.0), (76, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
