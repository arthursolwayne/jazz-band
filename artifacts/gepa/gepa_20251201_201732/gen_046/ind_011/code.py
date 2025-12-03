
import mido
from mido import Message, MidiFile, MidiTrack

# Create a new MIDI file
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set tempo to 160 BPM (MIDI tempo is in microseconds per beat)
track.append(mido.MetaMessage('set_tempo', tempo=375000, time=0))  # 60000000 / 160 = 375000

# Define MIDI notes for each instrument
# Tenor sax (you): A4 (69), B4 (71), C5 (60), D5 (62), E5 (64), F5 (65), G5 (67)
# Bass (Marcus): D2 (38), G2 (43), A2 (45), C3 (48), E3 (52)
# Piano (Diane): C4 (60), E4 (64), G4 (67), A4 (69), B4 (71), D5 (62)
# Drums (Little Ray): Kick (36), Snare (38), Hi-Hat (42)

# Bar 1: Little Ray (Drums) – sets the mood
track.append(Message('note_on', note=36, velocity=100, time=0))  # Kick on 1
track.append(Message('note_off', note=36, velocity=100, time=375))  # Kick off on 1
track.append(Message('note_on', note=38, velocity=100, time=375))  # Snare on 2
track.append(Message('note_off', note=38, velocity=100, time=375))  # Snare off on 2
track.append(Message('note_on', note=42, velocity=90, time=375))  # Hi-Hat on 3
track.append(Message('note_off', note=42, velocity=90, time=375))  # Hi-Hat off on 3
track.append(Message('note_on', note=38, velocity=100, time=375))  # Snare on 4
track.append(Message('note_off', note=38, velocity=100, time=375))  # Snare off on 4
track.append(Message('note_on', note=42, velocity=90, time=375))  # Hi-Hat on 1
track.append(Message('note_off', note=42, velocity=90, time=375))  # Hi-Hat off on 1
track.append(Message('note_on', note=42, velocity=90, time=375))  # Hi-Hat on 2
track.append(Message('note_off', note=42, velocity=90, time=375))  # Hi-Hat off on 2
track.append(Message('note_on', note=42, velocity=90, time=375))  # Hi-Hat on 3
track.append(Message('note_off', note=42, velocity=90, time=375))  # Hi-Hat off on 3
track.append(Message('note_on', note=42, velocity=90, time=375))  # Hi-Hat on 4
track.append(Message('note_off', note=42, velocity=90, time=375))  # Hi-Hat off on 4

# Bar 2: Diane (Piano) – opens with an Fmaj7, then moves to Am7
track.append(Message('note_on', note=60, velocity=90, time=375))  # C4 (Fmaj7)
track.append(Message('note_on', note=64, velocity=90, time=0))     # E4 (Fmaj7)
track.append(Message('note_on', note=67, velocity=90, time=0))     # G4 (Fmaj7)
track.append(Message('note_on', note=69, velocity=90, time=0))     # A4 (Fmaj7)
track.append(Message('note_off', note=60, velocity=90, time=375))  # C4 off
track.append(Message('note_off', note=64, velocity=90, time=375))  # E4 off
track.append(Message('note_off', note=67, velocity=90, time=375))  # G4 off
track.append(Message('note_off', note=69, velocity=90, time=375))  # A4 off

track.append(Message('note_on', note=57, velocity=90, time=375))  # A3 (Am7)
track.append(Message('note_on', note=60, velocity=90, time=0))     # C4 (Am7)
track.append(Message('note_on', note=64, velocity=90, time=0))     # E4 (Am7)
track.append(Message('note_on', note=69, velocity=90, time=0))     # A4 (Am7)
track.append(Message('note_off', note=57, velocity=90, time=375))  # A3 off
track.append(Message('note_off', note=60, velocity=90, time=375))  # C4 off
track.append(Message('note_off', note=64, velocity=90, time=375))  # E4 off
track.append(Message('note_off', note=69, velocity=90, time=375))  # A4 off

# Bar 3: Marcus (Bass) – walks F7 with chromatic approach
track.append(Message('note_on', note=43, velocity=80, time=375))  # G2 (F7 root)
track.append(Message('note_off', note=43, velocity=80, time=375)) # G2 off
track.append(Message('note_on', note=42, velocity=80, time=375))  # F#2 (chromatic approach)
track.append(Message('note_off', note=42, velocity=80, time=375)) # F#2 off
track.append(Message('note_on', note=48, velocity=80, time=375))  # C3 (F7 5th)
track.append(Message('note_off', note=48, velocity=80, time=375)) # C3 off
track.append(Message('note_on', note=45, velocity=80, time=375))  # A2 (F7 3rd)
track.append(Message('note_off', note=45, velocity=80, time=375)) # A2 off

# Bar 4: You (Tenor Sax) – motif, two phrases with space
track.append(Message('note_on', note=69, velocity=110, time=375))  # A4 (note 1)
track.append(Message('note_off', note=69, velocity=110, time=375)) # A4 off
track.append(Message('note_on', note=71, velocity=110, time=375))  # B4 (note 2)
track.append(Message('note_off', note=71, velocity=110, time=375)) # B4 off
track.append(Message('note_on', note=67, velocity=110, time=375))  # G4 (note 3)
track.append(Message('note_off', note=67, velocity=110, time=375)) # G4 off
track.append(Message('note_on', note=69, velocity=110, time=375))  # A4 (note 4)
track.append(Message('note_off', note=69, velocity=110, time=375)) # A4 off

track.append(Message('note_on', note=71, velocity=110, time=375))  # B4 (note 5)
track.append(Message('note_off', note=71, velocity=110, time=375)) # B4 off
track.append(Message('note_on', note=67, velocity=110, time=375))  # G4 (note 6)
track.append(Message('note_off', note=67, velocity=110, time=375)) # G4 off
track.append(Message('note_on', note=64, velocity=110, time=375))  # E4 (note 7)
track.append(Message('note_off', note=64, velocity=110, time=375)) # E4 off
track.append(Message('note_on', note=69, velocity=110, time=375))  # A4 (note 8)
track.append(Message('note_off', note=69, velocity=110, time=375)) # A4 off

# Save the MIDI file
mid.save('jazz_intro.mid')
