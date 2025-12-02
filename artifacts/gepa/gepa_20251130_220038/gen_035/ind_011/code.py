
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Fill the bar with hihat, kick on 1 and 3, snare on 2 and 4
for i in range(4):
    time = i * 0.375
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.1875, end=time + 0.1875 + 0.375)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm, chromatic approach to F
bass_notes = [pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.5 + 0.375),  # F
              pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=1.875 + 0.375), # Eb
              pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.25 + 0.375),  # Gb
              pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.625 + 0.375)] # Ab
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=1.5 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.5 + 0.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.5 + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.5 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=2.625 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=2.625 + 0.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=2.625 + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=2.625 + 0.375)   # F
]
piano.notes.extend(piano_notes)

# Sax: motif - whisper at first, then a cry
sax_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=1.5, end=1.5 + 0.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=44, start=1.875, end=1.875 + 0.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.25 + 0.375),  # B
    pretty_midi.Note(velocity=100, pitch=46, start=2.625, end=2.625 + 0.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=2.625 + 0.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=2.625 + 0.375)   # B
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Fm, chromatic approach to F
bass_notes = [pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.0 + 0.375),  # F
              pretty_midi.Note(velocity=90, pitch=39, start=3.375, end=3.375 + 0.375), # Eb
              pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=3.75 + 0.375),  # Gb
              pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.125 + 0.375)] # Ab
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.0 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.0 + 0.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.0 + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.0 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.125 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=4.125, end=4.125 + 0.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=4.125, end=4.125 + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.125 + 0.375)   # F
]
piano.notes.extend(piano_notes)

# Sax: motif - whisper at first, then a cry
sax_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.0 + 0.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.375 + 0.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=3.75 + 0.375),  # B
    pretty_midi.Note(velocity=100, pitch=46, start=4.125, end=4.125 + 0.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.125 + 0.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.125 + 0.375)   # B
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Fm, chromatic approach to F
bass_notes = [pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.5 + 0.375),  # F
              pretty_midi.Note(velocity=90, pitch=39, start=4.875, end=4.875 + 0.375), # Eb
              pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.25 + 0.375),  # Gb
              pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.625 + 0.375)] # Ab
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.5 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.5 + 0.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.5 + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.5 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=5.625 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=5.625 + 0.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=5.625, end=5.625 + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=5.625 + 0.375)   # F
]
piano.notes.extend(piano_notes)

# Sax: motif - whisper at first, then a cry
sax_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.5 + 0.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=44, start=4.875, end=4.875 + 0.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.25 + 0.375),  # B
    pretty_midi.Note(velocity=100, pitch=46, start=5.625, end=5.625 + 0.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=44, start=5.625, end=5.625 + 0.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=5.625 + 0.375)   # B
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = 4.5 + i * 0.375
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.1875, end=time + 0.1875 + 0.375)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
