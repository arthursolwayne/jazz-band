
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
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    start = bar1_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    start = bar1_start + i * 0.75 + 0.1875
    snare = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    start = bar1_start + i * 0.375
    hihat = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.1875)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Fm7 -> Bbm7 -> Eb7 -> Am7
# Roots: F, Bb, Eb, A
# Walking line with chromatic approaches
bass_notes = [
    # Bar 2: Fm7 (F, Ab, D, C)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # C2

    # Bar 3: Bbm7 (Bb, Db, F, Eb)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # Db2
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # F2
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # Eb2

    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # Bb2
    pretty_midi.Note(velocity=100, pitch=73, start=5.625, end=6.0),  # D2

    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=77, start=6.0, end=6.375),  # A2
    pretty_midi.Note(velocity=100, pitch=72, start=6.375, end=6.75), # C2
    pretty_midi.Note(velocity=100, pitch=74, start=6.75, end=7.125), # E2
    pretty_midi.Note(velocity=100, pitch=71, start=7.125, end=7.5),  # G2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comping: open voicings, one chord per bar
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Eb2
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C2
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.875),  # D2

    # Bar 3: Bbm7 (Bb, Db, Eb, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # Db2
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Eb2
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F2

    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb2
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875),  # D2

    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=77, start=6.0, end=6.375),  # A2
    pretty_midi.Note(velocity=100, pitch=72, start=6.0, end=6.375),  # C2
    pretty_midi.Note(velocity=100, pitch=74, start=6.0, end=6.375),  # E2
    pretty_midi.Note(velocity=100, pitch=71, start=6.0, end=6.375),  # G2
]

for note in piano_notes:
    piano.notes.append(note)

# Sax melody: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, C (Fm scale)
# Bar 2: F, Ab, Bb
# Bar 3: C, F, Ab, Bb
# Bar 4: C, F, Ab, C

sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F2
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),   # Eb2
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # Bb2

    # Bar 3
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.5),  # C2
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.75),  # F2
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0),  # Eb2
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # Bb2

    # Bar 4
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.75),  # C2
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=5.0),   # F2
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25),  # Eb2
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.5),  # C2
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: continue on bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

for bar_start in [bar2_start, bar3_start, bar4_start]:
    kick_notes = [36, 36]
    snare_notes = [38, 38]
    hihat_notes = [42] * 8

    for i, note in enumerate(kick_notes):
        start = bar_start + i * 0.75
        kick = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
        drums.notes.append(kick)

    for i, note in enumerate(snare_notes):
        start = bar_start + i * 0.75 + 0.1875
        snare = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
        drums.notes.append(snare)

    for i, note in enumerate(hihat_notes):
        start = bar_start + i * 0.375
        hihat = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
