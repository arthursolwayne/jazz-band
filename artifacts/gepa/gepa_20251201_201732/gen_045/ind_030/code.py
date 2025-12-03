
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass (Marcus) - walking line starting on F (D2 is enharmonic to E#1, but we'll use D2 as F in 4th octave)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0), # F
]
bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings, one chord per bar, resolve on the last
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=2.25), # E
    # Bar 3: Bm7b5 (B, D, F, A)
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=3.0), # B
    pretty_midi.Note(velocity=100, pitch=78, start=2.25, end=3.0), # D
    pretty_midi.Note(velocity=100, pitch=80, start=2.25, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=82, start=2.25, end=3.0), # A
    # Bar 4: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.75), # F
]
piano.notes.extend(piano_notes)

# Sax (Dante) - short motif, starts on bar 2, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75), # E
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass (Marcus) - walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5), # F
]
bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings
piano_notes = [
    # Bar 3: Bm7b5 (B, D, F, A) - same as before, but transposed
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.75), # B
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=80, start=3.0, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.75), # A
    # Bar 4: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.5), # G
    pretty_midi.Note(velocity=100, pitch=78, start=3.75, end=4.5), # Bb
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.5), # F
]
piano.notes.extend(piano_notes)

# Sax (Dante) - continues motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5), # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass (Marcus) - walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=80, pitch=41, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0), # F
]
bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings
piano_notes = [
    # Bar 4: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.25), # F
    # Bar 5: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=6.0), # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=6.0), # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=6.0), # C
    pretty_midi.Note(velocity=100, pitch=78, start=5.25, end=6.0), # E
]
piano.notes.extend(piano_notes)

# Sax (Dante) - finishes motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0), # Bb
]
sax.notes.extend(sax_notes)

# Drums continue with the same rhythm for bars 2-4
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend([note for note in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
