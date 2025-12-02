
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

# Bass line (Marcus) - Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.25), # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # F2 (root)
    
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.375),  # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75), # C3 (fifth of next chord)
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125), # B2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=68, start=4.125, end=4.5),  # A2 (fifth)
    
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # C3 (fifth of next chord)
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25), # E3 (fifth of next chord)
    pretty_midi.Note(velocity=90, pitch=73, start=5.25, end=5.625), # D3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # C3 (fifth)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - Open voicings, different chord each bar, resolve on the last
# Bar 2 - Fmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A2 (major 3rd)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C3 (fifth)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # E3 (major 7th)
    
    # Bar 3 - Gm7
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G2 (root)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B2 (minor 3rd)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # D3 (fifth)
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),  # F3 (minor 7th)
    
    # Bar 4 - C7
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C2 (root)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E2 (major 3rd)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B2 (major 7th)
    
    # Bar 4 - Am7 (resolve)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # A2 (root)
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),  # C2 (minor 3rd)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # E2 (fifth)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # G2 (minor 7th)
]
piano.notes.extend(piano_notes)

# Saxophone (Dante) - Short motif, one phrase, make it sing
# Starts on F4 (66), moves to A4 (69), then E4 (64), then resolves on F4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.6875),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=1.6875, end=1.875), # A4
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0625), # E4
    pretty_midi.Note(velocity=110, pitch=66, start=2.0625, end=2.25),  # F4
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 + (bar - 2) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875)
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875)

drums.notes.extend([n for n in locals() if isinstance(n, pretty_midi.Note)])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
