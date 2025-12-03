
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
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.0, end=bar1_start + 0.1),
              pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.75, end=bar1_start + 0.85)]
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.375, end=bar1_start + 0.475),
               pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.125, end=bar1_start + 1.225)]
hihat_notes = [pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + i * 0.375, end=bar1_start + i * 0.375 + 0.05) for i in range(4)]
drums.notes.extend(kick_notes + snare_notes + hihat_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line in Fm (F, Ab, D, C), with chromatic approaches
bass_notes = []
bar_start = 1.5
bar_duration = 1.5
for i in range(3):  # 3 bars
    bar = bar_start + i * bar_duration
    # F (F2), Ab (Ab2), D (D2), C (C2)
    # Chromatic approaches: Eb just before F, Gb just before Ab, C# just before D, B just before C
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=53, start=bar + 0.0, end=bar + 0.1))  # F2
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=50, start=bar + 0.25, end=bar + 0.35))  # Eb2
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=51, start=bar + 0.5, end=bar + 0.6))  # Ab2
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=52, start=bar + 0.75, end=bar + 0.85))  # Gb2
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=55, start=bar + 1.0, end=bar + 1.1))  # D2
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=54, start=bar + 1.25, end=bar + 1.35))  # C#2
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=53, start=bar + 1.5, end=bar + 1.6))  # C2
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=52, start=bar + 1.75, end=bar + 1.85))  # B2

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on last
piano_notes = []
chords = [
    # Bar 2: Fm7 (F, Ab, C, D)
    [53, 50, 52, 55],
    # Bar 3: Bb7 (Bb, D, F, Ab)
    [57, 55, 53, 50],
    # Bar 4: Eb7 (Eb, G, Bb, D)
    [58, 60, 57, 55]
]

for i, chord in enumerate(chords):
    bar = bar_start + i * bar_duration
    # Play each chord on beats 2 and 4 (0.375 and 1.125 seconds into the bar)
    for beat_offset in [0.375, 1.125]:
        for pitch in chord:
            piano_notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=bar + beat_offset, end=bar + beat_offset + 0.1))

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
bar = bar_start
# Motif: F (53), Ab (50), C (52), F (53)
motif = [53, 50, 52, 53]
# Play the first two notes on beat 1, last two on beat 3
sax_notes.append(pretty_midi.Note(velocity=110, pitch=motif[0], start=bar + 0.0, end=bar + 0.1))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=motif[1], start=bar + 0.0, end=bar + 0.1))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=motif[2], start=bar + 0.75, end=bar + 0.85))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=motif[3], start=bar + 0.75, end=bar + 0.85))

sax.notes.extend(sax_notes)

# Drums: Continue the pattern for bars 2-4
for i in range(3):  # 3 bars
    bar = bar_start + i * bar_duration
    kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=bar + 0.0, end=bar + 0.1),
                  pretty_midi.Note(velocity=100, pitch=36, start=bar + 0.75, end=bar + 0.85)]
    snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=bar + 0.375, end=bar + 0.475),
                   pretty_midi.Note(velocity=100, pitch=38, start=bar + 1.125, end=bar + 1.225)]
    hihat_notes = [pretty_midi.Note(velocity=80, pitch=42, start=bar + i * 0.375, end=bar + i * 0.375 + 0.05) for i in range(4)]
    drums.notes.extend(kick_notes + snare_notes + hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
