
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drums.notes.append(drum_note)

drum_note = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.75)
drums.notes.append(drum_note)

drum_note = pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125)
drums.notes.append(drum_note)

drum_note = pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.5)
drums.notes.append(drum_note)

# Bar 2: Everyone in (1.5 - 3.0s)
# Bass line - chromatic walking line
bass_note = pretty_midi.Note(velocity=90, pitch=46, start=1.5, end=1.875)
bass.notes.append(bass_note)

bass_note = pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25)
bass.notes.append(bass_note)

bass_note = pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.625)
bass.notes.append(bass_note)

bass_note = pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0)
bass.notes.append(bass_note)

# Piano comping on 2 and 4
piano_note = pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.125)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.125)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=2.875)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=2.875)
piano.notes.append(piano_note)

# Drums continue
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drums.notes.append(drum_note)

drum_note = pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25)
drums.notes.append(drum_note)

drum_note = pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)
drums.notes.append(drum_note)

drum_note = pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0)
drums.notes.append(drum_note)

# Saxophone motif - short and suspended
sax_note = pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875)
sax.notes.append(sax_note)

sax_note = pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625)
sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line - chromatic walking line
bass_note = pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375)
bass.notes.append(bass_note)

bass_note = pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75)
bass.notes.append(bass_note)

bass_note = pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125)
bass.notes.append(bass_note)

bass_note = pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5)
bass.notes.append(bass_note)

# Piano comping on 2 and 4
piano_note = pretty_midi.Note(velocity=95, pitch=62, start=3.375, end=3.625)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.625)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=95, pitch=62, start=4.125, end=4.375)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=95, pitch=67, start=4.125, end=4.375)
piano.notes.append(piano_note)

# Drums continue
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drums.notes.append(drum_note)

drum_note = pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75)
drums.notes.append(drum_note)

drum_note = pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)
drums.notes.append(drum_note)

drum_note = pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5)
drums.notes.append(drum_note)

# Saxophone motif - continuation and resolution
sax_note = pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375)
sax.notes.append(sax_note)

sax_note = pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125)
sax.notes.append(sax_note)

sax_note = pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5)
sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line - chromatic walking line
bass_note = pretty_midi.Note(velocity=90, pitch=54, start=4.5, end=4.875)
bass.notes.append(bass_note)

bass_note = pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25)
bass.notes.append(bass_note)

bass_note = pretty_midi.Note(velocity=90, pitch=56, start=5.25, end=5.625)
bass.notes.append(bass_note)

bass_note = pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0)
bass.notes.append(bass_note)

# Piano comping on 2 and 4
piano_note = pretty_midi.Note(velocity=95, pitch=62, start=4.875, end=5.125)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.125)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=95, pitch=62, start=5.625, end=5.875)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=95, pitch=67, start=5.625, end=5.875)
piano.notes.append(piano_note)

# Drums continue
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drums.notes.append(drum_note)

drum_note = pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25)
drums.notes.append(drum_note)

drum_note = pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)
drums.notes.append(drum_note)

drum_note = pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0)
drums.notes.append(drum_note)

# Saxophone motif - resolution
sax_note = pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875)
sax.notes.append(sax_note)

sax_note = pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625)
sax.notes.append(sax_note)

sax_note = pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0)
sax.notes.append(sax_note)

# Add hi-hat on every eighth
for i in range(0, 6, 0.375):
    if i < 1.5:
        continue
    if i % 0.75 == 0:
        continue
    drum_note = pretty_midi.Note(velocity=90, pitch=42, start=i, end=i + 0.375)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
