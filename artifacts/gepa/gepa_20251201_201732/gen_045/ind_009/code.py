
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

# Drums in Bar 1
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.75 + 0.375)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 1.875, end=bar1_start + 1.875 + 0.375)

# Hi-hats on every eighth
hihat_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=bar1_start + i * 0.375, end=bar1_start + i * 0.375 + 0.125)
    for i in range(4)
]

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - roots and fifths with chromatic approaches
bass_notes = []

bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bar 2: F7 (F, C, A, E)
# Root on 1, chromatic approach on 2, fifth on 3, root on 4
bass_notes.append(pretty_midi.Note(velocity=80, pitch=71, start=bar2_start, end=bar2_start + 0.375))  # F (D2)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=70, start=bar2_start + 0.375, end=bar2_start + 0.75))  # F#
bass_notes.append(pretty_midi.Note(velocity=80, pitch=74, start=bar2_start + 0.75, end=bar2_start + 1.125))  # C (fifth)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=71, start=bar2_start + 1.125, end=bar2_start + 1.5))  # F

# Bar 3: Bb7 (Bb, F, D, A)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=66, start=bar3_start, end=bar3_start + 0.375))  # Bb
bass_notes.append(pretty_midi.Note(velocity=80, pitch=67, start=bar3_start + 0.375, end=bar3_start + 0.75))  # B
bass_notes.append(pretty_midi.Note(velocity=80, pitch=71, start=bar3_start + 0.75, end=bar3_start + 1.125))  # F (fifth)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=66, start=bar3_start + 1.125, end=bar3_start + 1.5))  # Bb

# Bar 4: E7 (E, B, G#, D)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=69, start=bar4_start, end=bar4_start + 0.375))  # E
bass_notes.append(pretty_midi.Note(velocity=80, pitch=71, start=bar4_start + 0.375, end=bar4_start + 0.75))  # F
bass_notes.append(pretty_midi.Note(velocity=80, pitch=76, start=bar4_start + 0.75, end=bar4_start + 1.125))  # B (fifth)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=69, start=bar4_start + 1.125, end=bar4_start + 1.5))  # E

bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings, different chord each bar, resolve on last
piano_notes = []

# Bar 2: F7 - F, A, C, E
piano_notes.append(pretty_midi.Note(velocity=95, pitch=76, start=bar2_start, end=bar2_start + 0.75))  # E
piano_notes.append(pretty_midi.Note(velocity=95, pitch=71, start=bar2_start, end=bar2_start + 0.75))  # C
piano_notes.append(pretty_midi.Note(velocity=95, pitch=74, start=bar2_start, end=bar2_start + 0.75))  # A
piano_notes.append(pretty_midi.Note(velocity=95, pitch=77, start=bar2_start, end=bar2_start + 0.75))  # F

# Bar 3: Bb7 - Bb, D, F, A
piano_notes.append(pretty_midi.Note(velocity=95, pitch=71, start=bar3_start, end=bar3_start + 0.75))  # A
piano_notes.append(pretty_midi.Note(velocity=95, pitch=69, start=bar3_start, end=bar3_start + 0.75))  # F
piano_notes.append(pretty_midi.Note(velocity=95, pitch=66, start=bar3_start, end=bar3_start + 0.75))  # D
piano_notes.append(pretty_midi.Note(velocity=95, pitch=67, start=bar3_start, end=bar3_start + 0.75))  # Bb

# Bar 4: E7 - E, G#, B, D
piano_notes.append(pretty_midi.Note(velocity=95, pitch=65, start=bar4_start, end=bar4_start + 0.75))  # D
piano_notes.append(pretty_midi.Note(velocity=95, pitch=69, start=bar4_start, end=bar4_start + 0.75))  # B
piano_notes.append(pretty_midi.Note(velocity=95, pitch=71, start=bar4_start, end=bar4_start + 0.75))  # G#
piano_notes.append(pretty_midi.Note(velocity=95, pitch=69, start=bar4_start, end=bar4_start + 0.75))  # E

piano.notes.extend(piano_notes)

# Drums in Bars 2-4
# Bar 2
bar2_kick = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375)
bar2_snare = pretty_midi.Note(velocity=110, pitch=38, start=bar2_start + 0.75, end=bar2_start + 1.125)
bar2_hihat = [pretty_midi.Note(velocity=90, pitch=42, start=bar2_start + i * 0.375, end=bar2_start + i * 0.375 + 0.125) for i in range(4)]
drums.notes.extend([bar2_kick, bar2_snare] + bar2_hihat)

# Bar 3
bar3_kick = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375)
bar3_snare = pretty_midi.Note(velocity=110, pitch=38, start=bar3_start + 0.75, end=bar3_start + 1.125)
bar3_hihat = [pretty_midi.Note(velocity=90, pitch=42, start=bar3_start + i * 0.375, end=bar3_start + i * 0.375 + 0.125) for i in range(4)]
drums.notes.extend([bar3_kick, bar3_snare] + bar3_hihat)

# Bar 4
bar4_kick = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375)
bar4_snare = pretty_midi.Note(velocity=110, pitch=38, start=bar4_start + 0.75, end=bar4_start + 1.125)
bar4_hihat = [pretty_midi.Note(velocity=90, pitch=42, start=bar4_start + i * 0.375, end=bar4_start + i * 0.375 + 0.125) for i in range(4)]
drums.notes.extend([bar4_kick, bar4_snare] + bar4_hihat)

# Sax (Dante) - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []

# Motif: F, A, Bb, F (first two bars)
# Bar 2: F on beat 1, A on beat 2, Bb on beat 3, rest on beat 4
sax_notes.append(pretty_midi.Note(velocity=110, pitch=76, start=bar2_start, end=bar2_start + 0.375))  # F
sax_notes.append(pretty_midi.Note(velocity=110, pitch=79, start=bar2_start + 0.75, end=bar2_start + 1.125))  # A
sax_notes.append(pretty_midi.Note(velocity=110, pitch=77, start=bar2_start + 1.125, end=bar2_start + 1.5))  # Bb

# Bar 3: rest on beat 1, G# on beat 2, E on beat 3, Bb on beat 4 (resolve)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=bar3_start + 0.75, end=bar3_start + 1.125))  # G#
sax_notes.append(pretty_midi.Note(velocity=110, pitch=69, start=bar3_start + 1.125, end=bar3_start + 1.5))  # E

# Bar 4: rest on beat 1, F on beat 2, A on beat 3, Bb on beat 4 (resolve)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=76, start=bar4_start + 0.75, end=bar4_start + 1.125))  # F
sax_notes.append(pretty_midi.Note(velocity=110, pitch=79, start=bar4_start + 1.125, end=bar4_start + 1.5))  # A

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
