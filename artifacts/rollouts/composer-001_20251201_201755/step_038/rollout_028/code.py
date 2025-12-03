
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
bar_1_start = 0.0
bar_1_end = 1.5
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=bar_1_start + 0.0, end=bar_1_start + 0.375),
              pretty_midi.Note(velocity=100, pitch=36, start=bar_1_start + 1.125, end=bar_1_start + 1.5)]
snare_notes = [pretty_midi.Note(velocity=110, pitch=38, start=bar_1_start + 0.75, end=bar_1_start + 1.125),
               pretty_midi.Note(velocity=110, pitch=38, start=bar_1_start + 1.875, end=bar_1_start + 2.25)]
hihat_notes = []
for i in range(0, 4):
    hihat_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_1_start + i * 0.375, end=bar_1_start + i * 0.375 + 0.1875))
drums.notes.extend(kick_notes + snare_notes + hihat_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Marcus: Walking line (F2-A2, MIDI 53-58), roots and fifths with chromatic approaches
bar_2_start = 1.5
bar_3_start = 3.0
bar_4_start = 4.5

# Bass line - Fm7 -> Am7 -> Dm7 -> Gm7
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=bar_2_start, end=bar_2_start + 0.375),  # F2
    pretty_midi.Note(velocity=80, pitch=55, start=bar_2_start + 0.375, end=bar_2_start + 0.75),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=58, start=bar_2_start + 0.75, end=bar_2_start + 1.125),  # A2
    pretty_midi.Note(velocity=80, pitch=57, start=bar_2_start + 1.125, end=bar_2_start + 1.5),  # G2 (chromatic approach)

    pretty_midi.Note(velocity=80, pitch=58, start=bar_3_start, end=bar_3_start + 0.375),  # A2
    pretty_midi.Note(velocity=80, pitch=60, start=bar_3_start + 0.375, end=bar_3_start + 0.75),  # B2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=63, start=bar_3_start + 0.75, end=bar_3_start + 1.125),  # C#3
    pretty_midi.Note(velocity=80, pitch=62, start=bar_3_start + 1.125, end=bar_3_start + 1.5),  # C3 (chromatic approach)

    pretty_midi.Note(velocity=80, pitch=63, start=bar_4_start, end=bar_4_start + 0.375),  # C#3
    pretty_midi.Note(velocity=80, pitch=65, start=bar_4_start + 0.375, end=bar_4_start + 0.75),  # D#3 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=67, start=bar_4_start + 0.75, end=bar_4_start + 1.125),  # F3
    pretty_midi.Note(velocity=80, pitch=66, start=bar_4_start + 1.125, end=bar_4_start + 1.5),  # E3 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=bar_2_start, end=bar_2_start + 1.5),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=bar_2_start, end=bar_2_start + 1.5),  # Eb4
    pretty_midi.Note(velocity=100, pitch=69, start=bar_2_start, end=bar_2_start + 1.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=64, start=bar_2_start, end=bar_2_start + 1.5),  # C4
]

# Bar 3: Am7 (A, C, E, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=77, start=bar_3_start, end=bar_3_start + 1.5),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=bar_3_start, end=bar_3_start + 1.5),  # G4
    pretty_midi.Note(velocity=100, pitch=74, start=bar_3_start, end=bar_3_start + 1.5),  # A#4
    pretty_midi.Note(velocity=100, pitch=69, start=bar_3_start, end=bar_3_start + 1.5),  # E4
])

# Bar 4: Dm7 (D, F, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=74, start=bar_4_start, end=bar_4_start + 1.5),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=bar_4_start, end=bar_4_start + 1.5),  # F4
    pretty_midi.Note(velocity=100, pitch=76, start=bar_4_start, end=bar_4_start + 1.5),  # G#4
    pretty_midi.Note(velocity=100, pitch=72, start=bar_4_start, end=bar_4_start + 1.5),  # G4
])
piano.notes.extend(piano_notes)

# You: Tenor sax - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4, Ab4, F4, Eb4 (Fm7 arpeggio)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=bar_2_start, end=bar_2_start + 0.375),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=bar_2_start + 0.375, end=bar_2_start + 0.75),  # Ab4
    pretty_midi.Note(velocity=110, pitch=71, start=bar_2_start + 0.75, end=bar_2_start + 1.125),  # F4
    pretty_midi.Note(velocity=110, pitch=64, start=bar_2_start + 1.125, end=bar_2_start + 1.5),  # Eb4

    pretty_midi.Note(velocity=110, pitch=71, start=bar_4_start, end=bar_4_start + 0.375),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=bar_4_start + 0.375, end=bar_4_start + 0.75),  # Ab4
    pretty_midi.Note(velocity=110, pitch=71, start=bar_4_start + 0.75, end=bar_4_start + 1.125),  # F4
    pretty_midi.Note(velocity=110, pitch=64, start=bar_4_start + 1.125, end=bar_4_start + 1.5),  # Eb4
]
sax.notes.extend(sax_notes)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [bar_2_start, bar_3_start, bar_4_start]:
    kick_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    ]
    snare_notes = [
        pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    ]
    hihat_notes = []
    for i in range(0, 4):
        hihat_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875))
    drums.notes.extend(kick_notes + snare_notes + hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
