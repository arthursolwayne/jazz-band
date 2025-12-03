
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)  # Snare on 4 (next bar)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif starts here
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F7 (Ab)
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),  # D7 (F)
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # A7 (C)
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # F7 (Ab)
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D7 (F)
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),  # A7 (C)
]
sax.notes.extend(sax_notes)

# Bass: walking line in F (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.75),  # D2 (F)
    pretty_midi.Note(velocity=80, pitch=40, start=1.75, end=2.0),  # F2 (F)
    pretty_midi.Note(velocity=80, pitch=41, start=2.0, end=2.25),  # F#2 (F)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.5),  # A2 (F)
    pretty_midi.Note(velocity=80, pitch=40, start=2.5, end=2.75),  # F2 (F)
    pretty_midi.Note(velocity=80, pitch=38, start=2.75, end=3.0),  # D2 (F)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: F7 (F A C Eb) - open voicing
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=3.0),
    
    # Bar 3: Bb7 (Bb D F Ab) - open voicing
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),
    
    # Bar 4: E7 (E G# B D) - open voicing
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Drums (3.0 - 4.5s)
for i in range(3):
    start = 3.0 + i * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),  # Snare on 2
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 1.5),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.5),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),  # Kick on 3
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)  # Snare on 4
    ]
    drums.notes.extend(drum_notes)

# Bar 4: Drums (4.5 - 6.0s)
for i in range(3):
    start = 4.5 + i * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),  # Snare on 2
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 1.5),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.5),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),  # Kick on 3
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)  # Snare on 4
    ]
    drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
