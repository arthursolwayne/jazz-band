
import pretty_midi

# Create a new MIDI file with a tempo of 160 BPM (4/4 time)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Upright Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Set up tension with space and rhythm

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hi-Hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 2: Full ensemble begins (1.5 - 3.0s)
# Sax takes melody, piano comps, bass walks, drums continue

# Saxophone motif - short, emotional, incomplete
# Fm = F, Ab, Bb, D
# Start on Bb (Fm7), move up to D (Ab7), then to Ab, then rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=84, start=1.5, end=1.625))  # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=88, start=1.875, end=2.0))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=83, start=2.25, end=2.375)) # Ab

# Bass walking line in Fm
# F - Gb - Ab - A (chromatic approach)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.625))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=1.625, end=1.75)) # Gb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=1.875)) # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.0))  # A

# Piano: 7th chords on 2 and 4
# F7 = F, A, C, Eb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0))   # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.0))   # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0))   # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=2.0))   # Eb

# Bar 3: Continue the full ensemble (3.0 - 4.5s)
# Sax continues motif, incomplete but more developed
# Fm7 to Ab7
sax.notes.append(pretty_midi.Note(velocity=110, pitch=78, start=3.0, end=3.125))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=83, start=3.375, end=3.5))   # Ab
sax.notes.append(pretty_midi.Note(velocity=110, pitch=81, start=3.75, end=3.875))  # Bb

# Bass continues walking
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.125))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=3.125, end=3.25))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.375))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.5))   # C#

# Piano: F7 again
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.5))   # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.5))   # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5))   # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.5))   # Eb

# Bar 4: Resolution and tension (4.5 - 6.0s)
# Sax resolves the motif, ends on a sustained note
sax.notes.append(pretty_midi.Note(velocity=110, pitch=88, start=4.5, end=5.25))   # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=83, start=5.25, end=6.0))   # Ab

# Bass continues walking
bass.notes.append(pretty_midi.Note(velocity=80, pitch=73, start=4.5, end=4.625))  # Db
bass.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=4.625, end=4.75))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=75, start=4.75, end=4.875))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=4.875, end=5.0))   # E

# Piano: Back to F7 but with tension
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=6.0))   # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0))   # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0))   # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=6.0))   # Eb

# Drums continue with the same pattern
for i in range(4, 8):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro_in_Fm.mid")
