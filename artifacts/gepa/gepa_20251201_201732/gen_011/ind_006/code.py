
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
drums_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4 (outside bar 1)
]

drums.notes.extend(drums_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625), # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2 (root)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75), # A2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125), # F2
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # D2
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625), # F2
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # D2
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (Fmaj7)
    pretty_midi.Note(velocity=80, pitch=57, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # E
    
    # Bar 3 (Bb7)
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # A
    
    # Bar 4 (Cm7)
    pretty_midi.Note(velocity=80, pitch=58, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # Bb
]

piano.notes.extend(piano_notes)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 1.5)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.5)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)

drums.notes.extend([pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5) for start in [1.5, 2.25, 3.0, 3.75, 4.5, 5.25]])

# Sax: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F - A - Bb - F (F7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125), # F (return)
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
