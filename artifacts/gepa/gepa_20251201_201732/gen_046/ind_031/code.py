
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5), # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in F (F2 - C3), roots and fifths with chromatic approach
# Bar 2: F (root), E (chromatic approach), C (fifth), B (chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=80, pitch=73, start=1.875, end=2.25), # E2
    pretty_midi.Note(velocity=80, pitch=77, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=80, pitch=76, start=2.625, end=3.0), # B2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar, resolve on the last
# Bar 2: F7 with #11 (F A C E Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0), # F4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=3.0), # A4
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=3.0), # C5
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=3.0), # E5
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=3.0), # Bb4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, haunting and incomplete, starts on beat 2
# Motif: F (beat 2), Bb (beat 3), F (beat 4), rest on beat 1
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25), # F4 on beat 2
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # Bb4 on beat 3
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0), # F4 on beat 4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: G7 with #9 (G B D F A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=75, start=3.0, end=3.375), # G2
    pretty_midi.Note(velocity=80, pitch=78, start=3.375, end=3.75), # B2
    pretty_midi.Note(velocity=80, pitch=80, start=3.75, end=4.125), # D3
    pretty_midi.Note(velocity=80, pitch=77, start=4.125, end=4.5), # F3
]
bass.notes.extend(bass_notes)

# Piano: G7 with #9 (G B D F A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5), # G4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5), # B4
    pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=4.5), # D5
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=4.5), # F5
    pretty_midi.Note(velocity=80, pitch=79, start=3.0, end=4.5), # A5
]
piano.notes.extend(piano_notes)

# Sax: Repeat motif with slight variation, more intensity
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75), # F4 on beat 2
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125), # Bb4 on beat 3
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5), # F4 on beat 4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5), # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: F7 with #11 (F A C E Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=80, pitch=73, start=4.875, end=5.25), # E2
    pretty_midi.Note(velocity=80, pitch=77, start=5.25, end=5.625), # C3
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0), # B2
]
bass.notes.extend(bass_notes)

# Piano: F7 with #11 (F A C E Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0), # F4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=6.0), # A4
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=6.0), # C5
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=6.0), # E5
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=6.0), # Bb4
]
piano.notes.extend(piano_notes)

# Sax: Repeat motif with slight variation, more intensity
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25), # F4 on beat 2
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625), # Bb4 on beat 3
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0), # F4 on beat 4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0), # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
