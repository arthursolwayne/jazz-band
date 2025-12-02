
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
    # Bar 1: 0.0 - 1.5s
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.375), (42, 0.75), (42, 1.125),
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F2 (root), F#2 (chromatic approach), C3 (fifth), B2 (chromatic approach)
    (78, 1.5), (79, 1.75), (84, 2.0), (83, 2.25),
    # Bar 3: G2 (root), G#2 (chromatic), D3 (fifth), C#3 (chromatic)
    (80, 2.5), (81, 2.75), (87, 3.0), (86, 3.25),
    # Bar 4: A2 (root), A#2 (chromatic), E3 (fifth), D#3 (chromatic)
    (81, 3.5), (82, 3.75), (89, 4.0), (88, 4.25)
]
for note, time in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bn)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
# Bar 3: G7 (G, B, D, F)
# Bar 4: Am7 (A, C, E, G)
piano_notes = [
    # Bar 2
    (77, 1.5), (82, 1.5), (84, 1.5), (87, 1.5),
    # Bar 3
    (80, 2.5), (84, 2.5), (87, 2.5), (83, 2.5),
    # Bar 4
    (81, 3.5), (84, 3.5), (87, 3.5), (89, 3.5)
]
for note, time in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(pn)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (77), A (82), C (84), F (77)
sax_notes = [
    (77, 1.5), (82, 1.75), (84, 2.0), (77, 2.25),
    (77, 3.5), (82, 3.75), (84, 4.0), (77, 4.25)
]
for note, time in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
