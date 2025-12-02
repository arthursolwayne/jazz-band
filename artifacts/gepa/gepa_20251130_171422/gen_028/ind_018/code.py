
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum sounds
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_note = pretty_midi.Note(velocity=110, pitch=hihat, start=0.0, end=0.375)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=110, pitch=hihat, start=0.375, end=0.75)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=110, pitch=hihat, start=0.75, end=1.125)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=110, pitch=hihat, start=1.125, end=1.5)
drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm
bass_note = pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.875)  # F
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25)  # G
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=46, start=2.25, end=2.625)  # E
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.0)  # D
bass.notes.append(bass_note)

# Piano: F7, Bb7, Ab7
piano_note = pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=2.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625)
piano.notes.append(piano_note)

# Sax: Melody - Haunted, sparse, expressive
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)  # G
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0)  # A
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25)  # G
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5)  # F
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75)  # G
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0)  # A
sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_note = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375)  # C
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75)  # D
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)  # C
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5)  # Bb
bass.notes.append(bass_note)

# Piano: F7, Ab7, Bb7
piano_note = pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.125)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875)
piano.notes.append(piano_note)

# Sax: Melody continues, building tension
sax_note = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25)  # F
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5)  # G
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75)  # A
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0)  # G
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25)  # F
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5)  # G
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75)  # A
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0)  # G
sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_note = pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875)  # D
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=46, start=4.875, end=5.25)  # E
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=44, start=5.25, end=5.625)  # D
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)  # C
bass.notes.append(bass_note)

# Piano: F7, Bb7, F7
piano_note = pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=6.0)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0)
piano.notes.append(piano_note)

# Drums: Kick and snare
drum_note = pretty_midi.Note(velocity=110, pitch=kick, start=4.5, end=4.625)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=110, pitch=snare, start=4.625, end=4.75)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=110, pitch=kick, start=5.25, end=5.375)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=110, pitch=snare, start=5.375, end=5.5)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=110, pitch=kick, start=5.625, end=5.75)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=110, pitch=snare, start=5.75, end=5.875)
drums.notes.append(drum_note)

# Sax: Melody ends on a whisper
sax_note = pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0)  # G
sax.notes.append(sax_note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dante_intro.mid")
