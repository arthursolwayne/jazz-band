
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums in Bar 1 (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# 160 BPM = 0.375 seconds per beat
# Bar = 4 beats = 1.5 seconds
# Time step = 0.375 seconds

bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.75, end=bar1_start + 0.75 + 0.375)

# Snare on 2 and 4
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.375, end=bar1_start + 0.375 + 0.375)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.125, end=bar1_start + 1.125 + 0.375)

# Hihat on every eighth
hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar1_start, end=bar1_start + 0.1875)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + 0.375, end=bar1_start + 0.375 + 0.1875)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + 0.75, end=bar1_start + 0.75 + 0.1875)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + 1.125, end=bar1_start + 1.125 + 0.1875)

drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bar 2: Start of the melody
bar2_start = 1.5
bar2_end = 3.0

# Bass: Marcus - walking line in F minor (F, G, Ab, A, Bb, B, C, Db)
# F: 70, G: 71, Ab: 72, A: 73, Bb: 74, B: 76, C: 72, Db: 73
# Every beat, root or fifth, with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=70, start=bar2_start, end=bar2_start + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=bar2_start + 0.375, end=bar2_start + 0.375 + 0.375),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=bar2_start + 0.75, end=bar2_start + 0.75 + 0.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=74, start=bar2_start + 1.125, end=bar2_start + 1.125 + 0.375),  # Bb
]

bass.notes.extend(bass_notes)

# Piano: Diane - open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, Eb)
# Open voicings, voice leading from F7 to Bb7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=75, start=bar2_start, end=bar2_start + 0.375),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=82, start=bar2_start, end=bar2_start + 0.375),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=84, start=bar2_start, end=bar2_start + 0.375),  # C (C5)
    pretty_midi.Note(velocity=100, pitch=80, start=bar2_start, end=bar2_start + 0.375),  # Eb (Eb4)
]

piano.notes.extend(piano_notes)

# Sax: Dante - one short motif, make it sing
# Start it, leave it hanging, come back and finish it
# F to Ab to Bb to F (motif) in F minor
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=bar2_start, end=bar2_start + 0.375),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=bar2_start + 0.375, end=bar2_start + 0.375 + 0.375),  # Ab
    pretty_midi.Note(velocity=110, pitch=74, start=bar2_start + 0.75, end=bar2_start + 0.75 + 0.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=70, start=bar2_start + 1.125, end=bar2_start + 1.125 + 0.375),  # F
]

sax.notes.extend(sax_notes)

# Bar 3
bar3_start = 3.0
bar3_end = 4.5

# Bass: Marcus - walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=bar3_start, end=bar3_start + 0.375),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=bar3_start + 0.375, end=bar3_start + 0.375 + 0.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=74, start=bar3_start + 0.75, end=bar3_start + 0.75 + 0.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=bar3_start + 1.125, end=bar3_start + 1.125 + 0.375),  # B
]

bass.notes.extend(bass_notes)

# Piano: Diane - Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=bar3_start, end=bar3_start + 0.375),  # Bb (Bb4)
    pretty_midi.Note(velocity=100, pitch=76, start=bar3_start, end=bar3_start + 0.375),  # D (D5)
    pretty_midi.Note(velocity=100, pitch=74, start=bar3_start, end=bar3_start + 0.375),  # F (F5)
    pretty_midi.Note(velocity=100, pitch=72, start=bar3_start, end=bar3_start + 0.375),  # Ab (Ab4)
]

piano.notes.extend(piano_notes)

# Sax: Dante - mirror the motif, but with a twist
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=bar3_start, end=bar3_start + 0.375),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=bar3_start + 0.375, end=bar3_start + 0.375 + 0.375),  # Ab
    pretty_midi.Note(velocity=110, pitch=74, start=bar3_start + 0.75, end=bar3_start + 0.75 + 0.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=70, start=bar3_start + 1.125, end=bar3_start + 1.125 + 0.375),  # F
]

sax.notes.extend(sax_notes)

# Bar 4
bar4_start = 4.5
bar4_end = 6.0

# Bass: Marcus - walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=bar4_start, end=bar4_start + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=bar4_start + 0.375, end=bar4_start + 0.375 + 0.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=74, start=bar4_start + 0.75, end=bar4_start + 0.75 + 0.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=bar4_start + 1.125, end=bar4_start + 1.125 + 0.375),  # G
]

bass.notes.extend(bass_notes)

# Piano: Diane - F7 (F, A, C, Eb), resolves to F
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=75, start=bar4_start, end=bar4_start + 0.375),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=82, start=bar4_start, end=bar4_start + 0.375),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=84, start=bar4_start, end=bar4_start + 0.375),  # C (C5)
    pretty_midi.Note(velocity=100, pitch=80, start=bar4_start, end=bar4_start + 0.375),  # Eb (Eb4)
]

piano.notes.extend(piano_notes)

# Sax: Dante - finish the motif, bring it back with a little more emotion
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=bar4_start, end=bar4_start + 0.375),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=bar4_start + 0.375, end=bar4_start + 0.375 + 0.375),  # Ab
    pretty_midi.Note(velocity=110, pitch=74, start=bar4_start + 0.75, end=bar4_start + 0.75 + 0.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=70, start=bar4_start + 1.125, end=bar4_start + 1.125 + 0.375),  # F
]

sax.notes.extend(sax_notes)

# Drums in Bars 2-4 (1.5 - 6.0s)
# Same pattern as Bar 1, repeated
bar2_4_start = 1.5
bar2_4_end = 6.0

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_4_start, end=bar2_4_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_4_start + 1.5, end=bar2_4_start + 1.5 + 0.375)
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_4_start + 3.0, end=bar2_4_start + 3.0 + 0.375)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar2_4_start + 0.375, end=bar2_4_start + 0.375 + 0.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar2_4_start + 0.375 + 1.5, end=bar2_4_start + 0.375 + 1.5 + 0.375)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=bar2_4_start + 0.375 + 3.0, end=bar2_4_start + 0.375 + 3.0 + 0.375)

# Hihat on every eighth
hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start, end=bar2_4_start + 0.1875)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start + 0.375, end=bar2_4_start + 0.375 + 0.1875)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start + 0.75, end=bar2_4_start + 0.75 + 0.1875)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start + 1.125, end=bar2_4_start + 1.125 + 0.1875)
hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start + 1.5, end=bar2_4_start + 1.5 + 0.1875)
hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start + 1.875, end=bar2_4_start + 1.875 + 0.1875)
hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start + 2.25, end=bar2_4_start + 2.25 + 0.1875)
hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start + 2.625, end=bar2_4_start + 2.625 + 0.1875)
hihat9 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start + 3.0, end=bar2_4_start + 3.0 + 0.1875)
hihat10 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start + 3.375, end=bar2_4_start + 3.375 + 0.1875)
hihat11 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start + 3.75, end=bar2_4_start + 3.75 + 0.1875)
hihat12 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start + 4.125, end=bar2_4_start + 4.125 + 0.1875)
hihat13 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start + 4.5, end=bar2_4_start + 4.5 + 0.1875)
hihat14 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start + 4.875, end=bar2_4_start + 4.875 + 0.1875)
hihat15 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start + 5.25, end=bar2_4_start + 5.25 + 0.1875)
hihat16 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_4_start + 5.625, end=bar2_4_start + 5.625 + 0.1875)

drums.notes.extend([kick1, kick2, kick3, snare1, snare2, snare3, hihat1, hihat2, hihat3, hihat4, hihat5, hihat6, hihat7, hihat8, hihat9, hihat10, hihat11, hihat12, hihat13, hihat14, hihat15, hihat16])

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
