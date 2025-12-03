
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: Fm - F (root), Ab (fifth), Gb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # Gb2
    # Bar 3: Bbm - Bb (root), D (fifth), C (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=2.875), # Bb2
    pretty_midi.Note(velocity=90, pitch=49, start=2.875, end=3.25), # D2
    pretty_midi.Note(velocity=90, pitch=48, start=3.25, end=3.625), # C2
    # Bar 4: Ebm - Eb (root), G (fifth), F (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=46, start=3.625, end=3.875), # Eb2
    pretty_midi.Note(velocity=90, pitch=50, start=3.875, end=4.25), # G2
    pretty_midi.Note(velocity=90, pitch=49, start=4.25, end=4.625), # F2
    # Bar 4 continuation: Fm - F (root)
    pretty_midi.Note(velocity=90, pitch=44, start=4.625, end=5.0), # F2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 - F, Ab, C, Eb
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875), # Ab2
    pretty_midi.Note(velocity=80, pitch=52, start=1.5, end=1.875), # C3
    pretty_midi.Note(velocity=80, pitch=55, start=1.5, end=1.875), # Eb3
    # Bar 3: Bbm7 - Bb, D, F, Ab
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=2.875), # Bb2
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=2.875), # D2
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=2.875), # F3
    pretty_midi.Note(velocity=80, pitch=56, start=2.625, end=2.875), # Ab3
    # Bar 4: Ebm7 - Eb, G, Bb, Db
    pretty_midi.Note(velocity=80, pitch=46, start=3.625, end=3.875), # Eb2
    pretty_midi.Note(velocity=80, pitch=50, start=3.625, end=3.875), # G2
    pretty_midi.Note(velocity=80, pitch=54, start=3.625, end=3.875), # Bb3
    pretty_midi.Note(velocity=80, pitch=58, start=3.625, end=3.875), # Db3
    # Bar 4 resolution: Fm7 - F, Ab, C, Eb
    pretty_midi.Note(velocity=80, pitch=44, start=4.625, end=5.0), # F2
    pretty_midi.Note(velocity=80, pitch=48, start=4.625, end=5.0), # Ab2
    pretty_midi.Note(velocity=80, pitch=52, start=4.625, end=5.0), # C3
    pretty_midi.Note(velocity=80, pitch=55, start=4.625, end=5.0), # Eb3
]
piano.notes.extend(piano_notes)

# Saxophone: short motif, make it sing, start it, leave it hanging
# Motif: F - Gb - Ab - Bb
# Start at bar 2, leave it hanging on the 3rd note, come back at bar 4 to finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.0), # F2
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.125), # Gb2
    pretty_midi.Note(velocity=100, pitch=48, start=2.125, end=2.25), # Ab2
    # Leave it hanging
    # Come back at bar 4 to complete the motif
    pretty_midi.Note(velocity=100, pitch=46, start=4.875, end=5.0), # Bb2
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 2.25)
bar2_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.25),
]
# Bar 3 (2.25 - 3.0)
bar3_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.875), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
]
# Bar 4 (3.0 - 3.75)
bar4_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.625), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
]
# Bar 4 continuation (3.75 - 4.5)
bar4_continuation_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.375), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
# Bar 4 final (4.5 - 5.0)
bar4_final_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
]
drums.notes.extend(bar2_drum_notes + bar3_drum_notes + bar4_drum_notes + bar4_continuation_drum_notes + bar4_final_drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
