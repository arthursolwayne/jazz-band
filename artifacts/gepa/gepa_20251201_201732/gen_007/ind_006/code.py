
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
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36]
snare_notes = [38]
hihat_notes = [42]

# Kick on 1 and 3
kick_times = [bar1_start + 0.0, bar1_start + 0.75]
for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_times = [bar1_start + 0.375, bar1_start + 1.125]
for time in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

# Hihat on every eighth
hihat_times = [bar1_start + 0.0, bar1_start + 0.375, bar1_start + 0.75, bar1_start + 1.125]
for time in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bass line: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (D2) => chromatic approach (E2)
    pretty_midi.Note(velocity=80, pitch=38, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=37, start=bar2_start + 0.375, end=bar2_start + 0.75),
    # Bar 2: C (G2) => chromatic approach (G#2)
    pretty_midi.Note(velocity=80, pitch=43, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + 1.125, end=bar2_start + 1.5),

    # Bar 3: Bb (A2) => chromatic approach (A#2)
    pretty_midi.Note(velocity=80, pitch=41, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=40, start=bar3_start + 0.375, end=bar3_start + 0.75),
    # Bar 3: F (D2) => chromatic approach (E2)
    pretty_midi.Note(velocity=80, pitch=37, start=bar3_start + 0.75, end=bar3_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=38, start=bar3_start + 1.125, end=bar3_start + 1.5),

    # Bar 4: Bb (A2) => chromatic approach (A#2)
    pretty_midi.Note(velocity=80, pitch=41, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=40, start=bar4_start + 0.375, end=bar4_start + 0.75),
    # Bar 4: F (D2) => chromatic approach (E2)
    pretty_midi.Note(velocity=80, pitch=37, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=38, start=bar4_start + 1.125, end=bar4_start + 1.5)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
# Bar 4: F7 (F, A, C, Eb)
piano_notes = []

# Bar 2: Fmaj7 (F, A, C, E) - 0.0 to 1.5s
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=bar2_start, end=bar2_start + 1.5),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=bar2_start, end=bar2_start + 1.5),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=bar2_start, end=bar2_start + 1.5),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=bar2_start, end=bar2_start + 1.5)   # E
])

# Bar 3: Bbmaj7 (Bb, D, F, Ab) - 1.5 to 3.0s
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=70, start=bar3_start, end=bar3_start + 1.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=73, start=bar3_start, end=bar3_start + 1.5),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=bar3_start, end=bar3_start + 1.5),  # F
    pretty_midi.Note(velocity=100, pitch=78, start=bar3_start, end=bar3_start + 1.5)   # Ab
])

# Bar 4: F7 (F, A, C, Eb) - 3.0 to 4.5s
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=bar4_start, end=bar4_start + 1.5),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=bar4_start, end=bar4_start + 1.5),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=bar4_start, end=bar4_start + 1.5),  # C
    pretty_midi.Note(velocity=100, pitch=77, start=bar4_start, end=bar4_start + 1.5)   # Eb
])

piano.notes.extend(piano_notes)

# Drums: same pattern as bar 1 for bars 2-4
for bar_start in [bar2_start, bar3_start, bar4_start]:
    # Kick on 1 and 3
    kick_times = [bar_start + 0.0, bar_start + 0.75]
    for time in kick_times:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)

    # Snare on 2 and 4
    snare_times = [bar_start + 0.375, bar_start + 1.125]
    for time in snare_times:
        note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)

    # Hihat on every eighth
    hihat_times = [bar_start + 0.0, bar_start + 0.375, bar_start + 0.75, bar_start + 1.125]
    for time in hihat_times:
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
        drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (71), G (72), Bb (70), F (71)
# Bar 2: Start
note1 = pretty_midi.Note(velocity=110, pitch=71, start=bar2_start, end=bar2_start + 0.75)
note2 = pretty_midi.Note(velocity=110, pitch=72, start=bar2_start + 0.75, end=bar2_start + 1.125)
note3 = pretty_midi.Note(velocity=110, pitch=70, start=bar2_start + 1.125, end=bar2_start + 1.5)
note4 = pretty_midi.Note(velocity=110, pitch=71, start=bar4_start, end=bar4_start + 0.375)

sax.notes.extend([note1, note2, note3, note4])

midi.instruments.extend([sax, bass, piano, drums])
midi.save('jazz_intro.mid')
