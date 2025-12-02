
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # F2 (root)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75), # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.125), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=46, start=4.125, end=4.5),  # G2 (root)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=46, start=4.5, end=4.875),  # G2 (root)
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.25), # A2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625), # C3 (fifth)
    pretty_midi.Note(velocity=100, pitch=49, start=5.625, end=6.0),  # B2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Diane, open voicings, resolve on the last beat of each bar
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C (fifth)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # G (seventh)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C (octave)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F# (chromatic)
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # D (fifth)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # A (seventh)
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # D (octave)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # C (fifth)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # G (seventh)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # C (octave)
]
piano.notes.extend(piano_notes)

# Sax: Dante, one short motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # G (F7)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb (F7)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F (F7)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # A (F7)
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875)
    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375)

drums.notes.extend([note for note in drums.notes if note.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
