
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [0.0, 1.5, 3.0, 4.5]
snare_times = [0.75, 2.25, 3.75, 5.25]
hihat_times = [i * 0.375 for i in range(0, 16)]

for t in kick_times:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125))
for t in snare_times:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125))
for t in hihat_times:
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.125))

# Bar 2: Full ensemble
# Start with sax melody

# Sax motif (Fm scale: F, Gb, Ab, A, Bb, B, C, Db)
# Motif: F, Ab, Bb, F (melodic fragment)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=61, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25)   # F
]
sax.notes.extend(sax_notes)

# Bass line: walking in Fm
# F, Gb, Ab, A, Bb, B, C, Db
# Chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=61, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=58, start=5.0, end=5.25)   # Db
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# F7 on 2, Bb7 on 4
# F7: F, A, Bb, C
# Bb7: Bb, D, Eb, F
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=61, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=63, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=4.0, end=4.25)   # F
]
piano.notes.extend(piano_notes)

# Bar 3: Sax melody (repeat motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=61, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25)   # F
]
sax.notes.extend(sax_notes)

# Bass line: walking in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=4.0, end=4.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=61, start=5.0, end=5.25)   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=90, pitch=61, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.25),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Sax melody (finish motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=6.0, end=6.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=61, start=6.5, end=6.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=7.0, end=7.25)   # F
]
sax.notes.extend(sax_notes)

# Bass line: walking in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=6.0, end=6.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=62, start=6.5, end=6.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=61, start=7.0, end=7.25)   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=6.0, end=6.25),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=6.0, end=6.25),  # A
    pretty_midi.Note(velocity=90, pitch=61, start=6.0, end=6.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=6.0, end=6.25),  # C
]
piano.notes.extend(piano_notes)

# Drums: continue for full 6 seconds
kick_times = [1.5, 3.0, 4.5, 6.0]
snare_times = [2.25, 3.75, 5.25, 6.75]
hihat_times = [i * 0.375 for i in range(4, 16)]

for t in kick_times:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125))
for t in snare_times:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125))
for t in hihat_times:
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
