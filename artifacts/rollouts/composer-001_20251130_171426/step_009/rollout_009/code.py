
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, never the same note twice.
# F minor scale: F, Gb, G, Ab, A, Bb, B, C
# Walking bass line in F minor: F, Gb, G, Ab, A, Bb, B, C
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.6875),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.6875, end=1.875),  # Gb
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0625),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=2.0625, end=2.25),   # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.4375),   # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.4375, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.8125),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=2.8125, end=3.0),    # C
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.1875),    # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.1875, end=3.375),  # Gb
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5625),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=3.5625, end=3.75),   # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=3.9375),   # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.9375, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.3125),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=4.3125, end=4.5),    # C
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.6875),    # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.6875, end=4.875),  # Gb
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.0625),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=5.0625, end=5.25),   # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.4375),   # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.4375, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=5.8125),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=5.8125, end=6.0),    # C
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
# F7 = F, A, C, Eb
# Bb7 = Bb, D, F, Ab
# F7 on 2 and 4 (bars 2 and 4)
# Each chord is 0.75 seconds
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.25),  # Eb
    
    # Bar 3 (2.25 - 3.0s) - rest
    # nothing
    
    # Bar 4 (3.0 - 3.75s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # Ab
    
    # Bar 5 (3.75 - 4.5s) - rest
    # nothing
    
    # Bar 6 (4.5 - 5.25s)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=5.25),  # Eb
    
    # Bar 7 (5.25 - 6.0s) - rest
    # nothing
]
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# F minor motif: F, Ab, Bb, C, F
# First 2 notes in bar 2, last 3 in bar 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=3.1875, end=3.375), # C
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.5625), # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
