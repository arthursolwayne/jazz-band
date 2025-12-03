
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
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.875), (39, 2.25), (43, 2.625),
    (43, 3.0), (45, 3.375), (44, 3.75), (48, 4.125),
    (48, 4.5), (50, 4.875), (49, 5.25), (53, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
piano_notes = [
    (62, 1.5), (65, 1.5), (67, 1.5), (71, 1.5),
    # Bar 3: G7 (B, D, G, B)
    (71, 3.0), (74, 3.0), (76, 3.0), (79, 3.0),
    # Bar 4: Cm7 (E, G, C, E)
    (64, 4.5), (67, 4.5), (69, 4.5), (72, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.75))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: D - F - G - D (MIDI 67, 69, 71, 67)
sax_notes = [
    (67, 1.5), (69, 1.875), (71, 2.25), (67, 2.625),
    (67, 4.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
