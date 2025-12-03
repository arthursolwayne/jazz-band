
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

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.875), (38, 2.25), (41, 2.625),
    (43, 3.0), (41, 3.375), (40, 3.75), (38, 4.125),
    (43, 4.5), (41, 4.875), (40, 5.25), (38, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, F)
piano_notes = [
    (62, 1.5), (64, 1.5), (67, 1.5), (69, 1.5),
    # Bar 3: Gm7 (Bb, D, G, Bb)
    (60, 3.0), (62, 3.0), (67, 3.0), (69, 3.0),
    # Bar 4: Cm7 (Eb, G, C, Eb)
    (63, 4.5), (67, 4.5), (60, 4.5), (63, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Motif: D (62) - F (64) - G (67) - D (62) - F (64) - G (67)
sax_notes = [
    (62, 1.5), (64, 1.5), (67, 1.5), (62, 2.0), (64, 2.25), (67, 2.5),
    (62, 3.0), (64, 3.25), (67, 3.5), (62, 4.0), (64, 4.25), (67, 4.5),
    (62, 5.0), (64, 5.25), (67, 5.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.125)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 0.875)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.5)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.25)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
