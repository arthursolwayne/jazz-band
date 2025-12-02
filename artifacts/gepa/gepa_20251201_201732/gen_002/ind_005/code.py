
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
kick_notes = [36]
snare_notes = [38]
hihat_notes = [42]

# Kick on 1 and 3
kick_times = [bar_1_start + 0.375, bar_1_start + 1.125]
for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_times = [bar_1_start + 0.75, bar_1_start + 1.5]
for time in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

# Hihat on every eighth
hihat_times = [bar_1_start + 0.375, bar_1_start + 0.75, bar_1_start + 1.125, bar_1_start + 1.5]
for time in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus on walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (38, 1.5, 1.6), (40, 1.6, 1.7), (38, 1.7, 1.8), (41, 1.8, 1.9),
    (43, 1.9, 2.0), (41, 2.0, 2.1), (38, 2.1, 2.2), (40, 2.2, 2.3),
    (43, 2.3, 2.4), (41, 2.4, 2.5), (38, 2.5, 2.6), (40, 2.6, 2.7),
    (38, 2.7, 2.8), (40, 2.8, 2.9), (38, 2.9, 3.0),
    
    # Bar 3 (3.0 - 4.5s)
    (38, 3.0, 3.1), (40, 3.1, 3.2), (38, 3.2, 3.3), (41, 3.3, 3.4),
    (43, 3.4, 3.5), (41, 3.5, 3.6), (38, 3.6, 3.7), (40, 3.7, 3.8),
    (43, 3.8, 3.9), (41, 3.9, 4.0), (38, 4.0, 4.1), (40, 4.1, 4.2),
    (38, 4.2, 4.3), (40, 4.3, 4.4), (38, 4.4, 4.5),
    
    # Bar 4 (4.5 - 6.0s)
    (38, 4.5, 4.6), (40, 4.6, 4.7), (38, 4.7, 4.8), (41, 4.8, 4.9),
    (43, 4.9, 5.0), (41, 5.0, 5.1), (38, 5.1, 5.2), (40, 5.2, 5.3),
    (43, 5.3, 5.4), (41, 5.4, 5.5), (38, 5.5, 5.6), (40, 5.6, 5.7),
    (38, 5.7, 5.8), (40, 5.8, 5.9), (38, 5.9, 6.0)
]

for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: Diane on open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, Db)
chords = [
    [65, 69, 72, 67],  # Fm7
    [71, 74, 76, 69],  # Bb7
    [64, 67, 71, 69],  # Eb7
]

for i, chord in enumerate(chords):
    bar_start = 1.5 + i * 1.5
    # Play on 2 and 4
    for j, pitch in enumerate(chord):
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar_start + 0.75, end=bar_start + 0.75 + 0.1)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar_start + 1.5, end=bar_start + 1.5 + 0.1)
        piano.notes.append(note)

# Sax: Dante on tenor, one short motif, make it sing
# Motif: F (65), Ab (67), G (67), F (65) over 2 bars
sax_notes = [
    (65, 1.5, 1.6), (67, 1.6, 1.7), (67, 1.7, 1.8), (65, 1.8, 1.9),
    (65, 2.25, 2.35), (67, 2.35, 2.45), (67, 2.45, 2.55), (65, 2.55, 2.65)
]

for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Drums: same pattern for bars 2-4
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick_times = [bar_start + 0.375, bar_start + 1.125]
    for time in kick_times:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)

    snare_times = [bar_start + 0.75, bar_start + 1.5]
    for time in snare_times:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)

    hihat_times = [bar_start + 0.375, bar_start + 0.75, bar_start + 1.125, bar_start + 1.5]
    for time in hihat_times:
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
