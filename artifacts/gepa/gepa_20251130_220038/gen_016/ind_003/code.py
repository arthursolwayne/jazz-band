
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
    time = bar1_start + (i * 0.75)
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    time = bar1_start + (i * 0.75) + 0.125
    snare = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    time = bar1_start + (i * 0.125)
    hihat = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(hihat)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, Fm7 to Bb7
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.75, end=2.0),   # Gb
    pretty_midi.Note(velocity=100, pitch=55, start=2.0, end=2.25),   # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=100, pitch=58, start=2.75, end=3.0),   # Gb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25),   # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=3.25, end=3.5),   # D
    pretty_midi.Note(velocity=100, pitch=57, start=3.5, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.0),   # Gb
    pretty_midi.Note(velocity=100, pitch=55, start=4.0, end=4.25),   # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=4.25, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=100, pitch=58, start=4.75, end=5.0),   # Gb
    pretty_midi.Note(velocity=100, pitch=55, start=5.0, end=5.25),   # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.5),   # D
    pretty_midi.Note(velocity=100, pitch=57, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=100, pitch=58, start=5.75, end=6.0),   # Gb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),   # C
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),   # D
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),   # C
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=100, pitch=57, start=3.5, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),   # C
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),   # D
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),   # C
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),   # D
    pretty_midi.Note(velocity=100, pitch=57, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),   # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm7 -> Bb7 -> Fm7 -> Bb7 -> Fm7
# F, Ab, D, Eb, F, Ab, D, Eb, F, Ab, D, Eb, F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=57, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=110, pitch=54, start=1.75, end=2.0),   # Ab
    pretty_midi.Note(velocity=110, pitch=55, start=2.0, end=2.25),   # Bb
    pretty_midi.Note(velocity=110, pitch=57, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=110, pitch=57, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=110, pitch=54, start=2.75, end=3.0),   # Ab
    pretty_midi.Note(velocity=110, pitch=55, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=110, pitch=57, start=3.25, end=3.5),   # D
    pretty_midi.Note(velocity=110, pitch=57, start=3.5, end=3.75),   # F
    pretty_midi.Note(velocity=110, pitch=54, start=3.75, end=4.0),   # Ab
    pretty_midi.Note(velocity=110, pitch=55, start=4.0, end=4.25),   # Bb
    pretty_midi.Note(velocity=110, pitch=57, start=4.25, end=4.5),   # D
    pretty_midi.Note(velocity=110, pitch=57, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=110, pitch=54, start=4.75, end=5.0),   # Ab
    pretty_midi.Note(velocity=110, pitch=55, start=5.0, end=5.25),   # Bb
    pretty_midi.Note(velocity=110, pitch=57, start=5.25, end=5.5),   # D
    pretty_midi.Note(velocity=110, pitch=57, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=110, pitch=54, start=5.75, end=6.0),   # Ab
]
sax.notes.extend(sax_notes)

# Drums: continue
bar2_start = 1.5
bar2_end = 3.0
bar3_start = 3.0
bar3_end = 4.5
bar4_start = 4.5
bar4_end = 6.0

# Kick on 1 and 3
kick_notes = [36, 36]
for i, note in enumerate(kick_notes):
    time = bar2_start + (i * 0.75)
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(kick)

    time = bar3_start + (i * 0.75)
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(kick)

    time = bar4_start + (i * 0.75)
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(kick)

# Snare on 2 and 4
snare_notes = [38, 38]
for i, note in enumerate(snare_notes):
    time = bar2_start + (i * 0.75) + 0.125
    snare = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(snare)

    time = bar3_start + (i * 0.75) + 0.125
    snare = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(snare)

    time = bar4_start + (i * 0.75) + 0.125
    snare = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(snare)

# Hihat on every eighth
hihat_notes = [42] * 8
for i, note in enumerate(hihat_notes):
    time = bar2_start + (i * 0.125)
    hihat = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(hihat)

for i, note in enumerate(hihat_notes):
    time = bar3_start + (i * 0.125)
    hihat = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(hihat)

for i, note in enumerate(hihat_notes):
    time = bar4_start + (i * 0.125)
    hihat = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
