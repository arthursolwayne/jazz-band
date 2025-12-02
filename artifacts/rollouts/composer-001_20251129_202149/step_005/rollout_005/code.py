
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
midi.tempo_changes = [pretty_midi.TempoChange(120, 0.0)]

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125, 1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125, 3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125, 4.5, 4.6875, 4.875, 5.0625, 5.25]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: C - E - Bb - D (one short motif, leave it hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # D
]

sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=35, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=36, start=1.75, end=2.0),  # B
    pretty_midi.Note(velocity=80, pitch=37, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=39, start=2.25, end=2.5),  # D
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5),  # B
]

piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # E
]

sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=37, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=80, pitch=39, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=80, pitch=40, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=4.0, end=4.25),  # F#
    pretty_midi.Note(velocity=80, pitch=45, start=4.25, end=4.5),  # G
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.5),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=4.25, end=4.5),  # B
]

piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [4.5, 5.25]
snare_times = [4.875, 5.625]
hihat_times = [4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125, 6.0]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

# Sax: Repeat the motif again, this time fully
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # E
]

sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=80, pitch=48, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=80, pitch=52, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=5.75, end=6.0),  # C#
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=5.75, end=6.0),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=5.75, end=6.0),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=5.75, end=6.0),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=5.75, end=6.0),  # B
]

piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
