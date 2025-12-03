
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (MIDI 53) walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),   # F2
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),   # F2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=3.0),  # F (MIDI 71)
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=3.0),  # Ab (MIDI 67)
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=3.0),  # C (MIDI 72)
    pretty_midi.Note(velocity=80, pitch=73, start=1.5, end=3.0),  # D (MIDI 73)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # G (MIDI 66)
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),  # C (MIDI 62)
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75),  # G (MIDI 66)
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),  # C (MIDI 62)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Bb2 (MIDI 58) walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.375),   # Bb2
    pretty_midi.Note(velocity=90, pitch=56, start=3.375, end=3.75),  # A2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125),  # G2
    pretty_midi.Note(velocity=90, pitch=58, start=4.125, end=4.5),   # Bb2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=4.5),  # Bb (MIDI 68)
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=4.5),  # D (MIDI 71)
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=4.5),  # F (MIDI 71)
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=4.5),  # Ab (MIDI 67)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif continuation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),  # A (MIDI 69)
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),  # G (MIDI 67)
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),  # A (MIDI 69)
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),  # G (MIDI 67)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: same pattern, but with a fill on beat 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    # Fill on beat 3
    pretty_midi.Note(velocity=85, pitch=38, start=3.75, end=3.9375), # Snare fill
    pretty_midi.Note(velocity=85, pitch=42, start=3.9375, end=4.125),# Hihat fill
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: C2 (MIDI 60) walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),   # C2
    pretty_midi.Note(velocity=90, pitch=58, start=4.875, end=5.25),  # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625),  # A2
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # C2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=6.0),  # C (MIDI 72)
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=6.0),  # Eb (MIDI 67)
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=6.0),  # G (MIDI 71)
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=6.0),  # Bb (MIDI 68)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),  # G (MIDI 67)
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # C (MIDI 62)
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),  # G (MIDI 67)
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # C (MIDI 62)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: same pattern, but with a fill on beat 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    # Fill on beat 3
    pretty_midi.Note(velocity=85, pitch=38, start=5.25, end=5.4375), # Snare fill
    pretty_midi.Note(velocity=85, pitch=42, start=5.4375, end=5.625),# Hihat fill
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
