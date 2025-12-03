
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, roots and fifths with chromatic approaches
# D2 = MIDI 38, F#2 = 43, D2 again, chromatic approach

bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # F#2
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=80, pitch=37, start=2.625, end=3.0),  # chromatic approach

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75),  # A2 (fifth)
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=80, pitch=39, start=4.125, end=4.5),  # chromatic approach

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25),  # F#2
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=80, pitch=37, start=5.625, end=6.0),  # chromatic approach
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
# Bar 3: Dm7 (D, F, A, C)
# Bar 4: Dmaj7 (D, F#, A, C#)

piano_notes = [
    # Bar 2: D7
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.875),  # C#4

    # Bar 3: Dm7
    pretty_midi.Note(velocity=85, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=85, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.375),  # C4

    # Bar 4: Dmaj7
    pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.875),  # C#4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start of motif
# D4 (62), F#4 (67), A4 (69)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),

    # Bar 3: Leave it hanging with a space
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
    
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),
]
sax.notes.extend(sax_notes)

# Drums: continue for bars 2-4
# Kick on 1 and 3 of each bar
# Snare on 2 and 4
# Hi-hat on every eighth

for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
