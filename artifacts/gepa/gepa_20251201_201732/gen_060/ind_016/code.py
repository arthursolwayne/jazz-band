
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: Fm (F, C)
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=75, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625), # E♭ (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=3.0),  # F
    # Bar 3: B♭m (B♭, F)
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # B♭
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125), # A♭ (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),  # B♭
    # Bar 4: E♭m (E♭, B♭)
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # E♭
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25), # B♭
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625), # D♭ (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # E♭
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, A♭, C, D♭)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # E♭
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # B♭
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # D♭ (resolve)
    
    # Bar 3: B♭m7 (B♭, D♭, F, G)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # B♭
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # D♭
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # E♭ (resolve)
    
    # Bar 4: E♭m7 (E♭, G, B♭, C)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # E♭
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # B♭
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # D♭ (resolve)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - A♭ - D♭ - F (half note, half note, quarter note, quarter note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=3.0),  # F (half note)
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=4.5),  # E♭ (half note)
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=5.25), # D♭ (quarter note)
    pretty_midi.Note(velocity=110, pitch=70, start=5.25, end=6.0), # F (quarter note)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
