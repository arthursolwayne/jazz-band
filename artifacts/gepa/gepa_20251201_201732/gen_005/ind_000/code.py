
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.125),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375), (41, 1.875, 0.375), (43, 2.25, 0.375), (40, 2.625, 0.375),
    (38, 3.0, 0.375), (41, 3.375, 0.375), (43, 3.75, 0.375), (40, 4.125, 0.375),
    (38, 4.5, 0.375), (41, 4.875, 0.375), (43, 5.25, 0.375), (40, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Fm7 (F, Ab, C, Eb) -> Bb7 (Bb, D, F, Ab) -> E7 (E, G#, B, D) -> Amaj7 (A, C#, E, G#)
piano_notes = [
    (53, 1.5, 0.375), (60, 1.5, 0.375), (65, 1.5, 0.375), (64, 1.5, 0.375),  # Fm7
    (59, 2.25, 0.375), (67, 2.25, 0.375), (60, 2.25, 0.375), (64, 2.25, 0.375),  # Bb7
    (65, 3.0, 0.375), (69, 3.0, 0.375), (71, 3.0, 0.375), (67, 3.0, 0.375),  # E7
    (69, 3.75, 0.375), (74, 3.75, 0.375), (71, 3.75, 0.375), (76, 3.75, 0.375)   # Amaj7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 + (bar - 2) * 1.5
    # Kick on beat 1 and 3
    kick_start = bar_start
    kick_end = kick_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    kick_start = bar_start + 0.75
    kick_end = kick_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    # Snare on beat 2 and 4
    snare_start = bar_start + 0.375
    snare_end = snare_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    snare_start = bar_start + 1.125
    snare_end = snare_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    # Hihat on every eighth
    for i in range(4):
        hihat_start = bar_start + i * 0.375
        hihat_end = hihat_start + 0.125
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F (53), Ab (60), A (61), F (53), rest, then repeat
sax_notes = [
    (53, 1.5, 0.375), (60, 1.875, 0.375), (61, 2.25, 0.375), (53, 2.625, 0.375),
    (53, 4.5, 0.375), (60, 4.875, 0.375), (61, 5.25, 0.375), (53, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
