
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
bar1_start = 0.0
bar1_end = 1.5

# Kick on beat 1 and 3
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.0, end=bar1_start + 0.0 + 0.375),
              pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.125 + 0.375)]

# Snare on beat 2 and 4
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.75 + 0.375),
               pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.875, end=bar1_start + 1.875 + 0.375)]

# Hihat on every eighth note
hihat_notes = []
for i in range(8):
    start = bar1_start + i * 0.375
    hihat_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.125))

drums.notes.extend(kick_notes + snare_notes + hihat_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

bar2_start = 1.5
bar2_end = 3.0

# Marcus - Walking bass line in F (F2, C3, G2, D3, etc.)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=73, start=bar2_start, end=bar2_start + 0.375),  # F2
    pretty_midi.Note(velocity=80, pitch=72, start=bar2_start + 0.375, end=bar2_start + 0.75),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=76, start=bar2_start + 0.75, end=bar2_start + 1.125),  # C3 (F5)
    pretty_midi.Note(velocity=80, pitch=75, start=bar2_start + 1.125, end=bar2_start + 1.5),  # B2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=73, start=bar2_start + 1.5, end=bar2_start + 1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=72, start=bar2_start + 1.875, end=bar2_start + 2.25),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=76, start=bar2_start + 2.25, end=bar2_start + 2.625),  # C3
    pretty_midi.Note(velocity=80, pitch=75, start=bar2_start + 2.625, end=bar2_start + 3.0),  # B2
]

bass.notes.extend(bass_notes)

# Diane - Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=bar2_start, end=bar2_end),  # F
    pretty_midi.Note(velocity=100, pitch=81, start=bar2_start, end=bar2_end),  # A
    pretty_midi.Note(velocity=100, pitch=78, start=bar2_start, end=bar2_end),  # C
    pretty_midi.Note(velocity=100, pitch=83, start=bar2_start, end=bar2_end),  # E
]

# Bar 3: Gm7 (G, Bb, D, F)
# Bar 4: C7 (C, E, G, Bb)
# Resolve on the last bar
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=83, start=bar2_start + 1.5, end=bar2_end),  # G
    pretty_midi.Note(velocity=100, pitch=86, start=bar2_start + 1.5, end=bar2_end),  # Bb
    pretty_midi.Note(velocity=100, pitch=87, start=bar2_start + 1.5, end=bar2_end),  # D
    pretty_midi.Note(velocity=100, pitch=78, start=bar2_start + 1.5, end=bar2_end),  # F
    pretty_midi.Note(velocity=100, pitch=78, start=bar2_start + 3.0, end=bar2_end),  # C
    pretty_midi.Note(velocity=100, pitch=83, start=bar2_start + 3.0, end=bar2_end),  # E
    pretty_midi.Note(velocity=100, pitch=87, start=bar2_start + 3.0, end=bar2_end),  # G
    pretty_midi.Note(velocity=100, pitch=86, start=bar2_start + 3.0, end=bar2_end),  # Bb
])

piano.notes.extend(piano_notes)

# Little Ray - same as bar 1
bar2_kicks = [pretty_midi.Note(velocity=100, pitch=36, start=bar2_start + 0.0, end=bar2_start + 0.0 + 0.375),
              pretty_midi.Note(velocity=100, pitch=36, start=bar2_start + 1.125, end=bar2_start + 1.125 + 0.375)]
bar2_snare = [pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 0.75, end=bar2_start + 0.75 + 0.375),
              pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 1.875, end=bar2_start + 1.875 + 0.375)]
bar2_hihat = []
for i in range(8):
    start = bar2_start + i * 0.375
    bar2_hihat.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.125))

drums.notes.extend(bar2_kicks + bar2_snare + bar2_hihat)

# Bar 3: Full quartet (3.0 - 4.5s)

bar3_start = 3.0
bar3_end = 4.5

# Marcus - Walking bass line (D3, C3, F3, E3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=77, start=bar3_start, end=bar3_start + 0.375),  # D3
    pretty_midi.Note(velocity=80, pitch=76, start=bar3_start + 0.375, end=bar3_start + 0.75),  # C3
    pretty_midi.Note(velocity=80, pitch=81, start=bar3_start + 0.75, end=bar3_start + 1.125),  # F3
    pretty_midi.Note(velocity=80, pitch=80, start=bar3_start + 1.125, end=bar3_start + 1.5),  # E3
    pretty_midi.Note(velocity=80, pitch=77, start=bar3_start + 1.5, end=bar3_start + 1.875),  # D3
    pretty_midi.Note(velocity=80, pitch=76, start=bar3_start + 1.875, end=bar3_start + 2.25),  # C3
    pretty_midi.Note(velocity=80, pitch=81, start=bar3_start + 2.25, end=bar3_start + 2.625),  # F3
    pretty_midi.Note(velocity=80, pitch=80, start=bar3_start + 2.625, end=bar3_start + 3.0),  # E3
]

bass.notes.extend(bass_notes)

# Diane - Open voicings (Gm7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=83, start=bar3_start, end=bar3_end),  # G
    pretty_midi.Note(velocity=100, pitch=86, start=bar3_start, end=bar3_end),  # Bb
    pretty_midi.Note(velocity=100, pitch=87, start=bar3_start, end=bar3_end),  # D
    pretty_midi.Note(velocity=100, pitch=78, start=bar3_start, end=bar3_end),  # F
]

piano.notes.extend(piano_notes)

# Little Ray - same as bar 1
bar3_kicks = [pretty_midi.Note(velocity=100, pitch=36, start=bar3_start + 0.0, end=bar3_start + 0.0 + 0.375),
              pretty_midi.Note(velocity=100, pitch=36, start=bar3_start + 1.125, end=bar3_start + 1.125 + 0.375)]
bar3_snare = [pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 0.75, end=bar3_start + 0.75 + 0.375),
              pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 1.875, end=bar3_start + 1.875 + 0.375)]
bar3_hihat = []
for i in range(8):
    start = bar3_start + i * 0.375
    bar3_hihat.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.125))

drums.notes.extend(bar3_kicks + bar3_snare + bar3_hihat)

# Bar 4: Full quartet (4.5 - 6.0s)

bar4_start = 4.5
bar4_end = 6.0

# Marcus - Walking bass line (C3, Bb3, E3, D3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=76, start=bar4_start, end=bar4_start + 0.375),  # C3
    pretty_midi.Note(velocity=80, pitch=85, start=bar4_start + 0.375, end=bar4_start + 0.75),  # Bb3
    pretty_midi.Note(velocity=80, pitch=80, start=bar4_start + 0.75, end=bar4_start + 1.125),  # E3
    pretty_midi.Note(velocity=80, pitch=77, start=bar4_start + 1.125, end=bar4_start + 1.5),  # D3
    pretty_midi.Note(velocity=80, pitch=76, start=bar4_start + 1.5, end=bar4_start + 1.875),  # C3
    pretty_midi.Note(velocity=80, pitch=85, start=bar4_start + 1.875, end=bar4_start + 2.25),  # Bb3
    pretty_midi.Note(velocity=80, pitch=80, start=bar4_start + 2.25, end=bar4_start + 2.625),  # E3
    pretty_midi.Note(velocity=80, pitch=77, start=bar4_start + 2.625, end=bar4_start + 3.0),  # D3
]

bass.notes.extend(bass_notes)

# Diane - Open voicings (C7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=78, start=bar4_start, end=bar4_end),  # C
    pretty_midi.Note(velocity=100, pitch=83, start=bar4_start, end=bar4_end),  # E
    pretty_midi.Note(velocity=100, pitch=87, start=bar4_start, end=bar4_end),  # G
    pretty_midi.Note(velocity=100, pitch=85, start=bar4_start, end=bar4_end),  # Bb
]

piano.notes.extend(piano_notes)

# Little Ray - same as bar 1
bar4_kicks = [pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + 0.0, end=bar4_start + 0.0 + 0.375),
              pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + 1.125, end=bar4_start + 1.125 + 0.375)]
bar4_snare = [pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.75 + 0.375),
              pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 1.875, end=bar4_start + 1.875 + 0.375)]
bar4_hihat = []
for i in range(8):
    start = bar4_start + i * 0.375
    bar4_hihat.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.125))

drums.notes.extend(bar4_kicks + bar4_snare + bar4_hihat)

# Dante - Tenor sax
# One short motif, start it, leave it hanging, then come back and finish it.
# Start on F, then Bb, then D, then F again but leave it hanging

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=bar2_start + 0.0, end=bar2_start + 0.25),  # F
    pretty_midi.Note(velocity=100, pitch=80, start=bar2_start + 0.375, end=bar2_start + 0.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=bar2_start + 0.75, end=bar2_start + 1.0),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=bar2_start + 1.125, end=bar2_start + 1.375),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=bar4_start + 0.0, end=bar4_start + 0.25),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=bar4_start + 0.375, end=bar4_start + 0.625),  # D
    pretty_midi.Note(velocity=100, pitch=80, start=bar4_start + 0.75, end=bar4_start + 1.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=bar4_start + 1.125, end=bar4_start + 1.375),  # F
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
