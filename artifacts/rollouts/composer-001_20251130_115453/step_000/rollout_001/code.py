
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
for beat in [0, 1, 2, 3]:
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=beat * 0.375 + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=beat * 0.375 + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=beat * 0.375, end=beat * 0.375 + 0.125)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=1.6, end=1.7)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.7, end=1.8)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=1.8, end=1.9)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.9, end=2.0)
sax.notes.append(note)

# Bass line (chromatic approach)
note = pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.6)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=41, start=1.6, end=1.7)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=42, start=1.7, end=1.8)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=43, start=1.8, end=1.9)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=42, start=1.9, end=2.0)
bass.notes.append(note)

# Piano (7th chords on 2 and 4)
note = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75)
piano.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5)
piano.notes.append(note)

# Drums
for beat in [0, 1, 2, 3]:
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=(beat + 2) * 0.375, end=(beat + 2) * 0.375 + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=(beat + 2) * 0.375, end=(beat + 2) * 0.375 + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=(beat + 2) * 0.375, end=(beat + 2) * 0.375 + 0.125)
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody
note = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=3.1, end=3.2)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=3.2, end=3.3)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=3.3, end=3.4)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=3.4, end=3.5)
sax.notes.append(note)

# Bass line (chromatic approach)
note = pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.1)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=41, start=3.1, end=3.2)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=42, start=3.2, end=3.3)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=43, start=3.3, end=3.4)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=42, start=3.4, end=3.5)
bass.notes.append(note)

# Piano (7th chords on 2 and 4)
note = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25)
piano.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0)
piano.notes.append(note)

# Drums
for beat in [0, 1, 2, 3]:
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=(beat + 4) * 0.375, end=(beat + 4) * 0.375 + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=(beat + 4) * 0.375, end=(beat + 4) * 0.375 + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=(beat + 4) * 0.375, end=(beat + 4) * 0.375 + 0.125)
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody
note = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=4.6, end=4.7)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.7, end=4.8)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=4.8, end=4.9)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=4.9, end=5.0)
sax.notes.append(note)

# Bass line (chromatic approach)
note = pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.6)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=41, start=4.6, end=4.7)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=42, start=4.7, end=4.8)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=43, start=4.8, end=4.9)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=42, start=4.9, end=5.0)
bass.notes.append(note)

# Piano (7th chords on 2 and 4)
note = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75)
piano.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5)
piano.notes.append(note)

# Drums
for beat in [0, 1, 2, 3]:
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=(beat + 6) * 0.375, end=(beat + 6) * 0.375 + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=(beat + 6) * 0.375, end=(beat + 6) * 0.375 + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=(beat + 6) * 0.375, end=(beat + 6) * 0.375 + 0.125)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro_wayne.mid")
