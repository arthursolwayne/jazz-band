
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
bar_1_start = 0.0
bar_1_end = 1.5

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [bar_1_start + 0.0, bar_1_start + 0.75]
snare_times = [bar_1_start + 0.375, bar_1_start + 1.125]
hihat_times = [bar_1_start + 0.0, bar_1_start + 0.375, bar_1_start + 0.75, bar_1_start + 1.125, bar_1_start + 1.5]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 38, 100), (1.875, 40, 100), (2.25, 39, 100), (2.625, 43, 100),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 42, 100), (3.375, 40, 100), (3.75, 38, 100), (4.125, 43, 100),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 42, 100), (4.875, 40, 100), (5.25, 38, 100), (5.625, 43, 100)
]
for t, p, v in bass_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + 0.1)
    bass.notes.append(note)

# Piano: Diane - open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 62, 100), (1.5, 67, 100), (1.5, 71, 100), (1.5, 69, 100),
    # Bar 3: Gm7 (G, Bb, D, F)
    (3.0, 67, 100), (3.0, 71, 100), (3.0, 69, 100), (3.0, 65, 100),
    # Bar 4: Bb7 (Bb, D, F, Ab)
    (4.5, 64, 100), (4.5, 69, 100), (4.5, 67, 100), (4.5, 65, 100)
]
for t, p, v in piano_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + 0.1)
    piano.notes.append(note)

# Drums: continue same pattern for bars 2-4
bar_2_start = 1.5
bar_3_start = 3.0
bar_4_start = 4.5

for bar_start in [bar_2_start, bar_3_start, bar_4_start]:
    kick_times = [bar_start + 0.0, bar_start + 0.75]
    snare_times = [bar_start + 0.375, bar_start + 1.125]
    hihat_times = [bar_start + 0.0, bar_start + 0.375, bar_start + 0.75, bar_start + 1.125, bar_start + 1.5]

    for t in kick_times:
        note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
        drums.notes.append(note)

    for t in snare_times:
        note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
        drums.notes.append(note)

    for t in hihat_times:
        note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
        drums.notes.append(note)

# Sax: Dante - one short motif, make it sing
# The motif: D (62) -> B (67) -> C (60) -> D (62)
# Start on bar 2, bar 2 start = 1.5s
# Play the motif over the first two beats (1.5 to 2.25s), leave it hanging at C, then resolve on D in bar 4

sax_notes = [
    (1.5, 62, 110), (1.875, 67, 110), (2.25, 60, 110), (5.25, 62, 110)
]
for t, p, v in sax_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + 0.1)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
