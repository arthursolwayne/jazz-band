
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

# Drums: Bar 1 (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare
]
drums.notes.extend(drums_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
# D2-G2, MIDI 38-43, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=39, start=3.375, end=3.75), # D#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25), # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # G5
]
# Bar 3: Bbm7 (D, F, Bb, Eb) - open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # Bb4
])
# Bar 4: Gm7 (Bb, D, G, B) - open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # Eb5
])
# Bar 4: Resolve to Cm7 (Eb, G, C, Eb) - open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G4
])
piano.notes.extend(piano_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 2) * 1.5 + 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)
drums.notes.extend(drums_notes)

# Sax: One short motif, haunting, incomplete
# Bar 2: Start with a motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # F4
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625), # C5
    pretty_midi.Note(velocity=100, pitch=69, start=2.0625, end=2.25),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.4375),  # C5
    pretty_midi.Note(velocity=100, pitch=65, start=2.4375, end=2.625), # A4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.8125), # F4
]
# Bar 3: Rest, let it breathe
# Bar 4: Come back and finish it
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # F4
    pretty_midi.Note(velocity=100, pitch=65, start=4.6875, end=4.875), # A4
])
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
