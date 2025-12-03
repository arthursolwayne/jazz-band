
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))    # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))  # Snare on 4

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with chromatic approach to Fm7
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75))   # D2 - Fm root
bass.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=1.75, end=2.0))   # F2 - Fm5
bass.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=2.0, end=2.25))   # Eb2 - chromatic approach
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.5))   # D2 - Fm root
bass.notes.append(pretty_midi.Note(velocity=100, pitch=43, start=2.5, end=2.75))   # G2 - Fm7
bass.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=2.75, end=3.0))   # F2 - Fm5

# Piano: Open voicing, Fm7 (F, Ab, D, C) on bar 2
piano.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=3.0))   # F4
piano.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=3.0))   # Ab4
piano.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=3.0))   # Bb4
piano.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=3.0))   # C4

# Sax: Melody - short motif, incomplete
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875))   # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25))  # G4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625))  # C4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0))   # D4

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line with chromatic approach to Ab7
bass.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.25))   # F2 - Ab7 root
bass.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=3.25, end=3.5))   # A2 - Ab7 b7
bass.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=3.75))   # G2 - chromatic approach
bass.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.0))   # F2 - Ab7 root
bass.notes.append(pretty_midi.Note(velocity=100, pitch=46, start=4.0, end=4.25))   # C3 - Ab7 5
bass.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=4.25, end=4.5))   # A2 - Ab7 b7

# Piano: Open voicing, Ab7 (Ab, C, Eb, G) on bar 3
piano.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=3.0, end=4.5))   # Ab4
piano.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=4.5))   # C5
piano.notes.append(pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=4.5))   # Bb4
piano.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=4.5))   # Ab4
piano.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=4.5))   # F4

# Sax: Melody - continuation of the motif, incomplete
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375))   # G4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75))  # F4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125))  # C4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5))   # D4

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line with chromatic approach to Dm7
bass.notes.append(pretty_midi.Note(velocity=100, pitch=46, start=4.5, end=4.75))   # C3 - Dm7 root
bass.notes.append(pretty_midi.Note(velocity=100, pitch=49, start=4.75, end=5.0))   # D3 - Dm7 5
bass.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=5.0, end=5.25))   # Bb3 - chromatic approach
bass.notes.append(pretty_midi.Note(velocity=100, pitch=46, start=5.25, end=5.5))   # C3 - Dm7 root
bass.notes.append(pretty_midi.Note(velocity=100, pitch=51, start=5.5, end=5.75))   # F3 - Dm7 b7
bass.notes.append(pretty_midi.Note(velocity=100, pitch=49, start=5.75, end=6.0))   # D3 - Dm7 5

# Piano: Open voicing, Dm7 (D, F, A, C) on bar 4
piano.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=6.0))   # D4
piano.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=6.0))   # F4
piano.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=6.0))   # A4
piano.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=6.0))   # C4

# Sax: Melody - final note, unresolved
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875))   # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.25))  # G4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625))  # C4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0))   # D4

# Drums: Bar 4 (4.5 - 6.0s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)) # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625))# Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))   # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))# Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0)) # Snare on 4

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
