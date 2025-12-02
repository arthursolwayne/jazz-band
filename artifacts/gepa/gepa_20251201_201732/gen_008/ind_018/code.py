
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

# Marcus: Walking bass line in F (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # Bb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # C (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),  # Ab (chromatic approach)
    
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # F (root)
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75), # Bb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125), # C (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),  # Ab (chromatic approach)
    
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25), # Bb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # C (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),  # Ab (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=80, start=1.5, end=1.875),  # E
]
# Bar 3: Bb7 (Bb D F Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # Ab
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # Bb
])
piano.notes.extend(piano_notes)

# Dante: Sax melody, one short motif, start it, leave it hanging, finish it
# Motif: F - Bb - C - F (sax in F, so F is 66)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0625), # C
    pretty_midi.Note(velocity=100, pitch=66, start=2.0625, end=2.25), # F (resolve)
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.1875, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5625), # C
    pretty_midi.Note(velocity=100, pitch=66, start=3.5625, end=3.75), # F (resolve)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.0625), # C
    pretty_midi.Note(velocity=100, pitch=66, start=5.0625, end=5.25), # F (resolve)
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar, kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    bar_start = bar * 1.5
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

drums.notes.extend(drums.notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
