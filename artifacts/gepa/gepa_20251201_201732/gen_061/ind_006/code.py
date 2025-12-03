
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625), # Eb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # G2
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125), # Gb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # G2
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625), # F#2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on last
piano_notes = [
    # Bar 2 (1.5 - 3.0s): Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C5
    
    # Bar 3 (3.0 - 4.5s): Gm7 (G Bb D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # F5
    
    # Bar 4 (4.5 - 6.0s): Bbm7 (Bb D F Ab)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # F5
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=6.0),  # Ab5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D E F G A Bb C
# Motif: D (E) F G (A) Bb C
# Start on D, leave it hanging on A, come back and finish on Bb C

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875), # E4 (chromatic)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.125, end=2.25), # A4
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # A4
    # Come back and finish
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.625), # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75), # G4
    pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=2.875), # F#4 (chromatic)
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.0),  # F4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        start = bar_start + i * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)

drums.notes.extend([note for note in drums.notes if note.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
