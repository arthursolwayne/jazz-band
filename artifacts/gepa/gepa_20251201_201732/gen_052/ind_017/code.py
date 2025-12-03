
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875), # Fm root (F)
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25), # C (Fm 5th)
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625), # Bb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0), # F
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375), # Eb (Fm 3rd)
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75), # G (Fm 7th)
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125), # Ab (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5), # Eb
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.625), # B (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0), # F
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Fm7 (F, Ab, C, Eb) in bar 2
# Bb7 (Bb, D, F, Ab) in bar 3
# E7 (E, G#, B, D) in bar 4
# Comp on 2 and 4
piano_notes = [
    # Bar 2 (Fm7)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875), # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875), # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875), # C
    # Bar 3 (Bb7)
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.375), # Ab
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.375), # D
    # Bar 4 (E7)
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875), # E
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.875), # G#
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875), # B
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875), # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F - Gb - Ab - rest
# Then return with F - Bb - C - rest
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=110, pitch=50, start=1.875, end=2.0625), # Ab
    pretty_midi.Note(velocity=110, pitch=53, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=110, pitch=48, start=2.4375, end=2.625), # Bb
    pretty_midi.Note(velocity=110, pitch=55, start=2.625, end=2.8125), # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
