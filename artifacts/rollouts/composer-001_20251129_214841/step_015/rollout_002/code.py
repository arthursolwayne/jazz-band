
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    start = bar1_start + (i * 0.75)
    kick = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    start = bar1_start + (i * 0.75) + 0.125
    snare = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    start = bar1_start + (i * 0.125)
    hihat = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125)
    drums.notes.append(hihat)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Bass line: Walking line with chromatic approaches
bass_notes = [60, 61, 62, 64, 65, 67, 68, 69]
for i, note in enumerate(bass_notes):
    start = bar2_start + (i * 0.375)
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: C7 (C, E, B) on beat 2
    (60, 64, 71),
    # Bar 2: G7 (G, B, D) on beat 4
    (67, 71, 69)
]
for i, chord in enumerate(piano_notes):
    start = bar2_start + (i * 0.75) + 0.125
    for note in chord:
        piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375)
        piano.notes.append(piano_note)

# Sax: Motif - C, E, G, B (C major triad with a twist)
sax_notes = [60, 64, 67, 71]
for i, note in enumerate(sax_notes):
    start = bar2_start + (i * 0.375)
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5

# Bass line: Walking line with chromatic approaches
bass_notes = [71, 72, 73, 75, 76, 78, 79, 81]
for i, note in enumerate(bass_notes):
    start = bar3_start + (i * 0.375)
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: C7 (C, E, B) on beat 2
    (60, 64, 71),
    # Bar 3: G7 (G, B, D) on beat 4
    (67, 71, 69)
]
for i, chord in enumerate(piano_notes):
    start = bar3_start + (i * 0.75) + 0.125
    for note in chord:
        piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375)
        piano.notes.append(piano_note)

# Sax: Motif - D, F, A, C (C minor triad with a twist)
sax_notes = [62, 65, 69, 72]
for i, note in enumerate(sax_notes):
    start = bar3_start + (i * 0.375)
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0

# Bass line: Walking line with chromatic approaches
bass_notes = [81, 82, 83, 85, 86, 88, 89, 91]
for i, note in enumerate(bass_notes):
    start = bar4_start + (i * 0.375)
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: C7 (C, E, B) on beat 2
    (60, 64, 71),
    # Bar 4: G7 (G, B, D) on beat 4
    (67, 71, 69)
]
for i, chord in enumerate(piano_notes):
    start = bar4_start + (i * 0.75) + 0.125
    for note in chord:
        piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375)
        piano.notes.append(piano_note)

# Sax: Motif - E, G, B, D (C minor triad with a twist)
sax_notes = [64, 67, 71, 74]
for i, note in enumerate(sax_notes):
    start = bar4_start + (i * 0.375)
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar4_kick_notes = [36, 36]
bar4_snare_notes = [38, 38]
bar4_hihat_notes = [42] * 8

for i, note in enumerate(bar4_kick_notes):
    start = bar4_start + (i * 0.75)
    kick = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(bar4_snare_notes):
    start = bar4_start + (i * 0.75) + 0.125
    snare = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(bar4_hihat_notes):
    start = bar4_start + (i * 0.125)
    hihat = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125)
    drums.notes.append(hihat)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("jazz_intro.mid")
